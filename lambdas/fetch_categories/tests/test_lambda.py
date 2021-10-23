# -*- coding: utf-8 -*-
import json
import unittest
from pathlib import Path

from httmock import urlmatch, HTTMock

from fetch_categories.service import lambda_handler


@urlmatch(netloc='https://lelibros.online/')
def lelibros_mock():
    return Path('resources/le_libros/index.html').read_text()


class TestCategoriesLambda(unittest.TestCase):

    def test_fetch_categories_lambda_handler(self):
        with HTTMock(lelibros_mock):
            response = lambda_handler(None, None)
        if response is None:
            self.fail()
        self.assertEqual(response['statusCode'], 200)
        body = json.loads(response['body'])
        self.assertEqual(
            ['Aventura',
             'Biografías y Memorias',
             'Ciencia-Ficción',
             'Cuentos y crónicas',
             'Drama',
             'Ensayos',
             'Fantástico Ficción',
             'Humor',
             'Infanto y Juvenil',
             'Novela',
             'Policial',
             'Romántico',
             'Terror y Suspense',
             'Ciencias Exactas',
             'Ciencias Naturales',
             'Ciencias Sociales',
             'Autoayuda',
             'Deportes y Juegos',
             'Espiritualidad',
             'Viajes y Guías'],
            list(map(lambda category: category['title'], body))
        )


if __name__ == '__main__':
    unittest.main()
