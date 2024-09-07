import boto3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Boto3 client
ec2_client = boto3.client(
    'ec2',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION')
)

# Function to get the default VPC ID
def get_default_vpc_id():
    response = ec2_client.describe_vpcs(
        Filters=[{
            'Name': 'isDefault',
            'Values': ['true']
        }]
    )
    default_vpc = response['Vpcs'][0]['VpcId']
    print(f"Default VPC ID: {default_vpc}")
    return default_vpc

# Write the VPC ID to the .env file
def update_env_file(vpc_id):
    with open('.env', 'r') as file:
        lines = file.readlines()
    with open('.env', 'w') as file:
        for line in lines:
            if line.startswith("VPC_ID="):
                file.write(f"VPC_ID={vpc_id}\n")
            else:
                file.write(line)
    print(f"Updated .env with VPC_ID={vpc_id}")

# Main logic
if __name__ == "__main__":
    # Get the default VPC ID programmatically
    vpc_id = get_default_vpc_id()

    # Update the .env file with the VPC ID
    update_env_file(vpc_id)

    # Now you can access the VPC ID from the .env file anytime
    print(f"Loaded VPC ID from .env: {os.getenv('VPC_ID')}")
