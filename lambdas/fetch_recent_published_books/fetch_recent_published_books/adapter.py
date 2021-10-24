from bs4 import BeautifulSoup

from fetch_recent_published_books.schemas.response import FetchBooksRecord
from logic.href import code_from_href


def tag_to_book(tag) -> FetchBooksRecord:
    return FetchBooksRecord(
        code=code_from_href(tag.attrs['href']),
        title=tag.attrs['title'],
        image=tag.select_one('amp-img').attrs['src']
    )


def content_to_books(content: BeautifulSoup) -> list:
    raw_books = content.select('.list-books>ul>li>a:first-child')
    return list(map(tag_to_book, raw_books))
