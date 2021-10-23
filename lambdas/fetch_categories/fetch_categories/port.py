import requests
from bs4 import BeautifulSoup


def fetch_all():
    url = "https://lelibros.online/"
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')
