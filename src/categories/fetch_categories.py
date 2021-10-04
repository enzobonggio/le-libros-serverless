import json

import requests
from bs4 import BeautifulSoup

from helpers.href_helper import code_from_href


def lambda_handler(event, context):
    url = "https://lelibros.online/"

    page = requests.get(url)
    content = BeautifulSoup(page.content, 'html.parser')
    rawCategories = content.find('aside').select('li>a')
    categories = map(category_tag_mapping, rawCategories)
    return {
        'statusCode': 200,
        'body': json.dumps(list(categories))
    }


def category_tag_mapping(tag):
    return {
        'code': code_from_href(tag.attrs['href']),
        'title': tag.text
    }
