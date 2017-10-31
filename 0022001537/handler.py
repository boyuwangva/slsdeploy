import json
#test
def hello(event, context):
    body = {
        "message": "ver 2",
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

