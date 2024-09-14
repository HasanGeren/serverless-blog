import json
import boto3
import os
# import requests

s3_client = boto3.client('s3')

def lambda_handler(event, context):

    # Get the bucket name from environment variables
    bucket_name = os.environ.get('BUCKET_NAME')

    # Define the folder name (with trailing slash to create "folder" in S3)
    folder_name = 'test-folder/'

    try:
        # Create a "folder" by uploading an empty file with the folder path
        s3_client.put_object(Bucket=bucket_name, Key=folder_name)

        return {
            'statusCode': 200,
            'body': json.dumps(f"Folder {folder_name} created in bucket {bucket_name}")
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error creating folder: {str(e)}")
        }
