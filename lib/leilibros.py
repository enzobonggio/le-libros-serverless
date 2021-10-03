from books.fetch_books_by_category import lambda_handler as fetch_books_by_category_lambda_handler
from categories.fetch_categories import lambda_handler as fetch_categories_lambda_handler


def fetch_categories(event, context):
    return fetch_categories_lambda_handler(event, context)


def fetch_books_by_category(event, context):
    return fetch_books_by_category_lambda_handler(event, context)
