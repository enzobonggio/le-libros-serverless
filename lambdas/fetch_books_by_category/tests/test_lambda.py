# -*- coding: utf-8 -*-
import json
import unittest
from pathlib import Path

from httmock import urlmatch, HTTMock

from fetch_books_by_category.service import lambda_handler


@urlmatch(netloc='https://lelibros.online/categoria/aventura/')
def lelibros_mock():
    return Path('resources/le_libros/categoria/aventura.html').read_text()


class TestBooksLambda(unittest.TestCase):

    def test_fetch_books_by_category_lambda_handler(self):
        test_event = {
            'queryStringParameters':
                {
                    'category': 'aventura'
                }
        }

        with HTTMock(lelibros_mock):
            response = lambda_handler(test_event, None)
        if response is None:
            self.fail()
        self.assertEqual(200, response['statusCode'])
        body = json.loads(response['body'])
        metadata = body['metadata']
        records = body['records']
        self.assertEqual(1, metadata['page'])
        self.assertEqual(12, metadata['per_page'])
        self.assertEqual(10, metadata['page_count'])
        self.assertEqual(
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
             'Furia'],
            list(map(lambda record: record['title'], records))
        )


if __name__ == '__main__':
    unittest.main()
