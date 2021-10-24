# -*- coding: utf-8 -*-
import json
import unittest
from pathlib import Path

from httmock import urlmatch, HTTMock

from fetch_recent_published_books.service import lambda_handler


@urlmatch(netloc='https://lelibros.online/')
def lelibros_mock():
    return Path('resources/le_libros/index.html').read_text()


class TestBooksLambda(unittest.TestCase):

    def test_fetch_books_by_category_lambda_handler(self):
        test_event = {
            'queryStringParameters': {}
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
        self.assertEqual(216, metadata['page_count'])
        self.assertEqual(
            ['La Escapada',
             'El Experimento',
             'El Vizconde de Bragelonne',
             'Los Perros de la Guerra',
             'El Uso de los Placeres',
             'Cadena de Fuego',
             'El Río del Edén',
             'Crónicas de Bustos Domecq',
             'La Granja',
             'La Hija de Homero',
             'Vida y Destino',
             'Misterio del Ojo de Fuego'],
            list(map(lambda record: record['title'], records))
        )


if __name__ == '__main__':
    unittest.main()
