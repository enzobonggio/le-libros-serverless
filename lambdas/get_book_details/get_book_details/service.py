from get_book_details.controller import get_book_details


def lambda_handler(event, context):
    path_parameters = event['pathParameters']
    book = path_parameters['book_id']
    return get_book_details(book).to_json()
