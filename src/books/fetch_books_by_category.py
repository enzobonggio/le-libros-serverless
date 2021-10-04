import json

import requests
from bs4 import BeautifulSoup

from helpers.href_helper import code_from_href


def lambda_handler(event, context):
    category = event['queryStringParameters']['category']
    page_number = event['queryStringParameters'].get('page') or 1
    pageNumberHref = '/page/' + page_number + '/' if page_number > 1 else '/'
    url = "https://lelibros.online/categoria/" + category + pageNumberHref
    page = requests.get(url)
    content = BeautifulSoup(page.content, 'html.parser')
    raw_books = content.select('.list-books>ul>li>a:first-child')
    books = list(map(book_tag_mapping, raw_books))
    last_page = int(content.select_one('.pagination>ul>li>a:last-child').attrs['data-ci-pagination-page'])

    return {
        'statusCode': 200,
        'body': json.dumps({
            '_metadata':
                {
                    "page": page_number,
                    "per_page": len(books),
                    "page_count": last_page
                },
            'records': books
        })
    }


def book_tag_mapping(tag):
    return {
        'code': code_from_href(tag.attrs['href']),
        'title': tag.attrs['title'],
        'image': tag.select_one('amp-img').attrs['src']
    }
