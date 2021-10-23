from common_schemas.http_response import Response as HttpResponse


class Metadata:
    def __init__(self, page: int, per_page: int, page_count: int) -> None:
        self.page = page
        self.per_page = per_page
        self.page_count = page_count


class Body:
    def __init__(self, _metadata: Metadata, records: list) -> None:
        self.metadata = _metadata
        self.records = records


class Response(HttpResponse):
    def __init__(self, status: int, paginated_body: Body):
        super().__init__(status, paginated_body)
