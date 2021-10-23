import os

from bs4 import BeautifulSoup

from fetch_categories.schemas.response import FetchCategoryRecord
from logic.href import code_from_href
from logic.properties import load_properties

ic_resources = load_properties(
    os.path.join(os.path.dirname(__file__), '../resources/categories/ic_resources.properties'))


def tag_to_category(tag) -> FetchCategoryRecord:
    code = code_from_href(tag.attrs['href'])
    return FetchCategoryRecord(
        code=code,
        title=tag.text,
        image=ic_resources.get(code, '')
    )


def content_to_categories(content: BeautifulSoup) -> list:
    raw_categories = content.find('aside').select('li>a')
    return list(map(tag_to_category, raw_categories))
