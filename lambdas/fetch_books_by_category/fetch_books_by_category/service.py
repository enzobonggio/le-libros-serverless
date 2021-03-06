from fetch_books_by_category.controller import fetch_books_by_category


def lambda_handler(event, context):
    query_parameters = event['queryStringParameters']
    category = query_parameters['category']
    page_number = int(query_parameters.get('page') or '1')
    return fetch_books_by_category(category, page_number).to_json()
