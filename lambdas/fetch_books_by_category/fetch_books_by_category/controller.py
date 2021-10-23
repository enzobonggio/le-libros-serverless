from common_schemas.paginated_response import Response, Body
from adapters.page import content_to_page
from fetch_books_by_category.adapter import content_to_books
from fetch_books_by_category.port import fetch_by_category


def fetch_books_by_category(category: str, page_number: int):
    content = fetch_by_category(category, page=page_number)
    books = content_to_books(content)
    page = content_to_page(content, page=page_number, per_page=len(books))

    return Response(200, Body(page, books))
