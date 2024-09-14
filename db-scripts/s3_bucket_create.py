import boto3
from botocore.exceptions import ClientError

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize an S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'), 
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION')
)

def create_s3_bucket(bucket_name, region=None):
    try:
        if region is None:
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        print(f"Bucket {bucket_name} created successfully.")
    except ClientError as e:
        print(f"Error: {e}")
        return False
    return True

bucket_name = 'serverless-blog-platform-bucket'

# Create the S3 bucket
create_s3_bucket(bucket_name)
