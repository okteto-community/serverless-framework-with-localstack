import json


def hello(event, context):
    body = {
        "message": "Hello from Okteto!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
