from fetch_books_by_category.controller import fetch_books_by_category


def fetch_books_by_category_lambda_handler(event, context):
    query_parameters = event['queryStringParameters']
    category = query_parameters['category']
    page_number = query_parameters.get('page') or 1
    return fetch_books_by_category(category, page_number).to_json()
