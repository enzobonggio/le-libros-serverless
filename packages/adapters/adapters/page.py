from common_schemas.paginated_response import Metadata


def content_to_page(content, page: int, per_page: int):
    page_count = int(content.select_one('.pagination>ul>li>a:last-child').attrs['data-ci-pagination-page'])
    return Metadata(page_count=page_count, per_page=per_page, page=page)
