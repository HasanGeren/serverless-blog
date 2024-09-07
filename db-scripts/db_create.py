import boto3
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load RDS configuration from config.json
with open('./db-scripts/config.json') as config_file:
    config = json.load(config_file)

# Initialize the RDS client
rds_client = boto3.client(
    'rds',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION')
)

# Create the MySQL RDS instance
response = rds_client.create_db_instance(
    DBInstanceIdentifier='my-mysql-instance',
    AllocatedStorage=20,  # Storage in GB
    DBInstanceClass='db.t3.micro',  # Instance class for performance
    Engine='mysql',  # Database engine
    MasterUsername=config['MasterUsername'],  # Retrieve from config.json
    MasterUserPassword=config['MasterUserPassword'],  # Retrieve from config.json
    DBName='blog_platform_db',  # Initial database name
    BackupRetentionPeriod=7,  # Number of days to retain backups
    MultiAZ=False,  # True for Multi-AZ deployment for high availability
    PubliclyAccessible=True,  # True if you want the DB to be accessible over the internet
    StorageType='gp2',  # Storage type (general purpose SSD)
    VpcSecurityGroupIds=[os.getenv('VPC_SECURITY_GROUP_ID')],  # Retrieve from .env
)

# Print response from AWS RDS service
print("Creating RDS instance...")
print(response)
