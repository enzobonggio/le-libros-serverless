import re

from bs4 import BeautifulSoup
from logic.href import code_from_href

from fetch_recent_published_books.schemas.response import FetchBooksRecord


def tag_to_book(tag) -> FetchBooksRecord:
    code = code_from_href(tag.attrs['href'])
    code = re.search('descargar-libro-(.*)-en-.*', code).group(1)
    return FetchBooksRecord(
        code=code,
        title=tag.attrs['title'],
        image='https://lelibros.online' + tag.select_one('amp-img').attrs['src']
    )


def content_to_books(content: BeautifulSoup) -> list:
    raw_books = content.select('.list-books>ul>li>a:first-child')
    return list(map(tag_to_book, raw_books))
