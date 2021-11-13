from common_schemas.http_response import Response

from get_book_details.adapter import content_to_book_details
from get_book_details.port import get


def get_book_details(book):
    content = get(book)
    book_details = content_to_book_details(book, content)
    return Response(200, book_details)
