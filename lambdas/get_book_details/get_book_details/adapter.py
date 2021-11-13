from bs4 import BeautifulSoup, Tag

from get_book_details.schemas.response import BookDetails


def tag_to_link(tag: Tag) -> tuple:
    href = str(tag.attrs.get('href'))
    link_type = str(tag.attrs['title']).split(' ')[-1].upper()
    return  link_type, href


def content_to_book_details(code, content: BeautifulSoup) -> BookDetails:
    mobi_link = None
    epub_link = None
    pdf_link = None
    raw_book_details = content.select_one('.list-books>.livro')
    raw_book_links = content.select('.list-books>.links-livro>ul>li>a')

    for link in list(map(tag_to_link, raw_book_links)):
        if link[0] == 'EPUB':
            epub_link = link[1]
        elif link[0] == 'MOBI':
            mobi_link = link[1]
        elif link[0] == 'PDF':
            pdf_link = link[1]

    description = content.select_one('.list-books>.tabbed>.content-tabs>.tab1>ul>li').text
    title = raw_book_details.select_one('h2').text
    author = raw_book_details.select_one('strong>a:first-child').text
    image = 'https://lelibros.online' + raw_book_details.select_one('amp-img').attrs['src']

    return BookDetails(code=code, description=description, title=title, author=author, image=image, pdf_link=pdf_link,
                       mobi_link=mobi_link, epub_link=epub_link)
