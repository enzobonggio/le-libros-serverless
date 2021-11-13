from get_book_details.controller import get_book_details


def lambda_handler(event, context):
    print(str(event))
    query_parameters = event['queryStringParameters']
    book = query_parameters['book']
    return get_book_details(book).to_json()
