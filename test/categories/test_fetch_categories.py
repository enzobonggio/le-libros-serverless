# -*- coding: utf-8 -*-
import unittest
from pathlib import Path

from httmock import urlmatch, HTTMock

from lib.categories.fetch_categories import lambda_handler


@urlmatch(netloc='https://lelibros.online/')
def lelibros_mock():
    return Path('../resources/leilibros/index.html').read_text()


class FetchTest(unittest.TestCase):

    def test_fetch(self):
        with HTTMock(lelibros_mock):
            response = lambda_handler(None, None)
        if response is None:
            self.fail()
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(
            list(map(lambda category: category['title'], response['body'])),
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
             'Viajes y Guías']
        )


if __name__ == '__main__':
    unittest.main()
