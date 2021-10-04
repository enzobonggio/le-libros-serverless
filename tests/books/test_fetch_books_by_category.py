# -*- coding: utf-8 -*-
import json
import unittest
from pathlib import Path

from httmock import urlmatch, HTTMock

from src.books.fetch_books_by_category import lambda_handler


@urlmatch(netloc='https://lelibros.online/categoria/aventura/')
def lelibros_mock():
    return Path('../resources/leilibros/categoria/aventura.html').read_text()


class FetchTest(unittest.TestCase):

    def test_fetch(self):
        with HTTMock(lelibros_mock):
            response = lambda_handler(
                {
                    'queryStringParameters':
                        {
                            'category_href': 'categoria/aventura/'
                        }
                }
                , None)
        if response is None:
            self.fail()
        self.assertEqual(response['statusCode'], 200)
        body = json.loads(response['body'])
        metadata = body['_metadata']
        records = body['records']
        self.assertEqual(metadata['page'], 1)
        self.assertEqual(metadata['per_page'], 12)
        self.assertEqual(metadata['page_count'], 10)
        self.assertEqual(
            list(map(lambda record: record['title'], records)),
            ['El Vizconde de Bragelonne',
             'El Trono del Lobo Gris',
             'La Fragata Surprise',
             'Historias Asombrosas de la Segunda Guerra Mundial',
             'El Resurgir de la Atlántida',
             'Las Inquietudes de Shanti Andía',
             'La Asesina en el Submundo',
             'El Cantar de Shannara',
             'Veinte Años Después',
             'Arthas',
             'Centauros',
             'Furia'])


if __name__ == '__main__':
    unittest.main()
