import boto3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize an EC2 client
ec2_client = boto3.client(
    'ec2',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION')
)

# Function to create a security group
def create_security_group(group_name, description, vpc_id):
    try:
        response = ec2_client.create_security_group(
            GroupName=group_name,
            Description=description,
            VpcId=vpc_id
        )
        security_group_id = response['GroupId']
        print(f'Security Group Created: {security_group_id}')
        return security_group_id
    except Exception as e:
        print(f'Error creating security group: {e}')
        return None

# Function to add inbound rules to the security group
def authorize_security_group_ingress(security_group_id):
    try:
        response = ec2_client.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 3306,
                    'ToPort': 3306,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0', 'Description': 'Allow MySQL access from anywhere'}]
                }
            ]
        )
        print(f'Inbound rules set for {security_group_id}')
    except Exception as e:
        print(f'Error setting inbound rules: {e}')

# Main logic
if __name__ == "__main__":
    # Retrieve VPC ID from the .env file
    vpc_id = os.getenv('VPC_ID')

    if vpc_id:
        # Create the security group using the VPC ID from the .env file
        security_group_id = create_security_group('mysql-access-group', 'Security group for MySQL access', vpc_id)

        # Add inbound rules to allow MySQL traffic
        if security_group_id:
            authorize_security_group_ingress(security_group_id)
    else:
        print("VPC ID not found in .env file.")
