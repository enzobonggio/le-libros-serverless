from common_schemas.paginated_response import Response, Body
from adapters.page import content_to_page
from fetch_recent_published_books.adapter import content_to_books
from fetch_recent_published_books.port import fetch_recent_published


def fetch_recent_published_books(page_number: int):
    content = fetch_recent_published(page=page_number)
    books = content_to_books(content)
    page = content_to_page(content, page=page_number, per_page=len(books))

    return Response(200, Body(page, books))
