# -*- coding: utf-8 -*-
import json
import unittest
from pathlib import Path

from httmock import urlmatch, HTTMock

from get_book_details.service import lambda_handler


@urlmatch(netloc='https://lelibros.online/libro/descargar-libro-el-experimento-en-pdf-epub-mobi-o-leer-online/')
def lelibros_mock():
    return Path(
        'resources/le_libros/libro/descargar-libro-el-experimento-en-pdf-epub-mobi-o-leer-online.html').read_text()


class TestBooksLambda(unittest.TestCase):

    def test_fetch_books_by_category_lambda_handler(self):
        test_event = {
            'queryStringParameters':
                {
                    'book': 'el-experimento'
                }
        }

        with HTTMock(lelibros_mock):
            response = lambda_handler(test_event, None)
        if response is None:
            self.fail()
        self.assertEqual(200, response['statusCode'])
        body = json.loads(response['body'])
        self.assertEqual('El Experimento', body['title'])
        self.assertEqual('Sebastian Fitzek', body['author'])
        self.assertEqual(
            'https://lelibros.online/uploads/2017/07/descargar-libro-el-experimento-en-pdf-epub-mobi-o-leer-online.jpg',
            body['image'])
        self.assertEqual(
            'http://descargar.lelibros.online/Sebastian%20Fitzek/El%20Experimento%20('
            '535)/El%20Experimento%20-%20Sebastian%20Fitzek.epub',
            body['epub_link'])
        self.assertEqual(
            'http://descargar.lelibros.online/Sebastian%20Fitzek/El%20Experimento%20('
            '535)/El%20Experimento%20-%20Sebastian%20Fitzek.mobi',
            body['mobi_link'])

        self.assertEqual(
            'http://descargar.lelibros.online/Sebastian%20Fitzek/El%20Experimento%20('
            '535)/El%20Experimento%20-%20Sebastian%20Fitzek.pdf',
            body['pdf_link'])
        self.assertEqual('De la mano de su profesor, dos estudiantes de psicología participan en un experimento que '
                         'consiste en estudiar el expediente médico de un paciente de una clínica psiquiátrica privada '
                         'de Berlín, donde hace años tuvieron lugar escenas de horror y que, actualmente, se mantiene '
                         'cerrada al público. En medio de los acontecimientos se hallan el joven Caspar, un paciente '
                         'que sufre amnesia, incapaz de recordar quién es, y también un asesino en serie conocido como '
                         'el Destructor de almas. Tras el ataque a tres mujeres, el Destructor de almas centrará ahora '
                         'su objetivo en el centro psiquiátrico. Cualquiera puede ser la próxima víctima…',
                         body['description'])


if __name__ == '__main__':
    unittest.main()
