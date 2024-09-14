import json

from posts.get_posts import handle_get

def lambda_handler(event, context):
    http_method = event['httpMethod']
    path = event['path']

    # TBD: Add logic.
    if path == "/v1/posts":
        if http_method == "GET":
            return handle_get(event, context)
        return {
            'statusCode': 200,
           'body': json.dumps('To be handled')
        }
    return {
        "statusCode": 400,
        "body": json.dumps("Not found")
    }