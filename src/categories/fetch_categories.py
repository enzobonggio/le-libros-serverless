import json

import requests
from bs4 import BeautifulSoup


def lambda_handler(event, context):
    url = "https://lelibros.online/"

    page = requests.get(url)
    content = BeautifulSoup(page.content, 'html.parser')
    rawCategories = content.find('aside').select('li>a')
    categories = map(lambda tag: {'href': tag.attrs['href'], 'title': tag.text}, rawCategories)
    return {
        'statusCode': 200,
        'body': json.dump(list(categories))
    }
