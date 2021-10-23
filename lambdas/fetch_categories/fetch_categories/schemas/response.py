from common_schemas.http_response import Response


class FetchCategoryRecord:
    def __init__(self, code: str, title: str, image: str):
        self.code = code
        self.title = title
        self.image = image


class FetchCategoriesResponse(Response):
    def __init__(self, status: int, categories: list):
        super().__init__(status, categories)
