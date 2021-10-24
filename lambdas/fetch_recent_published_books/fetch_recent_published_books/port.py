import requests
from bs4 import BeautifulSoup


def fetch_recent_published(page: int):
    pageNumberHref = 'page/' + str(page) + '/' if page > 1 else '/'
    url = "https://lelibros.online/" + pageNumberHref
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')
