import requests
from bs4 import BeautifulSoup


def fetch_by_category(category: str, page: int):
    pageNumberHref = '/page/' + str(page) + '/' if page > 1 else '/'
    url = "https://lelibros.online/categoria/" + category + pageNumberHref
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')
