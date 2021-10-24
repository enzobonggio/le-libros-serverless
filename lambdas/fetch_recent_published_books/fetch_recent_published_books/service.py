from fetch_recent_published_books.controller import fetch_recent_published_books


def lambda_handler(event, context):
    query_parameters = event['queryStringParameters']
    page_number = query_parameters.get('page') or 1
    return fetch_recent_published_books(page_number).to_json()
