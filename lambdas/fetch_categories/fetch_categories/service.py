from fetch_categories.controller import fetch_categories


def fetch_categories_lambda_handler(event, context):
    return fetch_categories().to_json()
