import requests
from bs4 import BeautifulSoup


def lambda_handler(event, context):
    category_href = event['category_href']
    pageNumber = event.get('page') or 1
    url = "https://lelibros.online/" + category_href
    page = requests.get(url)
    content = BeautifulSoup(page.content, 'html.parser')
    raw_books = content.select('.list-books>ul>li>a:first-child')
    books = list(map(book_tag_mapping, raw_books))
    last_page = int(content.select_one('.pagination>ul>li>a:last-child').attrs['data-ci-pagination-page'])

    return {
        'statusCode': 200,
        'body': {
            '_metadata':
                {
                    "page": pageNumber,
                    "per_page": len(books),
                    "page_count": last_page
                },
            'records': books
        }
    }


def book_tag_mapping(tag):
    return {
        'href': tag.attrs['href'],
        'title': tag.attrs['title'],
        'image': tag.select_one('amp-img').attrs['src']
    }
