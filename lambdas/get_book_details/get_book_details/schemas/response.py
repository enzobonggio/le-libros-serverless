from common_schemas.http_response import Response


class BookDetails:
    def __init__(self, code, title, author, image, epub_link, mobi_link, pdf_link, description):
        self.code = code
        self.title = title
        self.author = author
        self.image = image
        self.epub_link = epub_link
        self.mobi_link = mobi_link
        self.pdf_link = pdf_link
        self.description = description


class GetBookDetailsResponse(Response):
    def __init__(self, status: int, book_detail: BookDetails):
        super().__init__(status, book_detail)
