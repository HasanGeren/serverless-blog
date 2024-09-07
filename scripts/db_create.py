import boto3

# Initialize the RDS client
rds_client = boto3.client('rds')

# Create the MySQL RDS instance
response = rds_client.create_db_instance(
    DBInstanceIdentifier='my-mysql-instance',
    AllocatedStorage=20,  # Storage in GB
    DBInstanceClass='db.t3.micro',  # Instance class for performance
    Engine='mysql',  # Database engine
    MasterUsername='admin',  # Master user for the DB
    MasterUserPassword='password123',  # Master user password
    DBName='blog_platform_db',  # Initial database name
    BackupRetentionPeriod=7,  # Number of days to retain backups
    MultiAZ=False,  # True for Multi-AZ deployment for high availability
    PubliclyAccessible=True,  # True if you want the DB to be accessible over the internet
    StorageType='gp2',  # Storage type (general purpose SSD)
    VpcSecurityGroupIds=['sg-XXXXXXXX'],  # Security group ID for DB access
)

# Print response from AWS RDS service
print("Creating RDS instance...")
print(response)