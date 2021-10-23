from common_schemas.paginated_response import Body, Response


class FetchBooksRecord:
    def __init__(self, code: str, title: str, image: str):
        self.code = code
        self.title = title
        self.image = image


class FetchBooksResponse(Response):
    def __init__(self, status: int, body: Body):
        super().__init__(status, body)
