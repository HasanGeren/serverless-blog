import json

# Dummy data. TODO: Remove when connected to db.
dummy_posts = [
    {"id": "dztzGL", "title": "Perennial Trees",
     "body": "Perennial trees are trees that live for multiple years, often many decades or even centuries."},
    {"id": "1Yroaq", "title": "Solar flares",
     "body": "A solar flare is a sudden, intense burst of radiation and energy on the Sun's surface that occurs when "
             "magnetic energy stored in the Sun's atmosphere is rapidly released."}
]


def handle_get(event, context):
    try:
        # Dummy implementation
        return {
            "statusCode": 200,
            "body": json.dumps(dummy_posts),
            "headers": {
                "Content-Type": "application/json"
            }
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers": {
                "Content-Type": "application/json"
            }
        }