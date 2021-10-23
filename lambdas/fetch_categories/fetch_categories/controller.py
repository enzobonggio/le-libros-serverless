from common_schemas.http_response import Response
from fetch_categories.adapter import content_to_categories
from fetch_categories.port import fetch_all


def fetch_categories():
    content = fetch_all()
    categories = content_to_categories(content)

    return Response(200, categories)
