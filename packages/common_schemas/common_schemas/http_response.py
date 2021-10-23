import json
from json import JSONEncoder


class Response:
    def __init__(self, status: int, body):
        self.status = status
        self.body = body

    def to_json(self):
        return {
            'statusCode': self.status,
            'body': json.dumps(self.body, cls=BodyDecoder)
        }


class BodyDecoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
