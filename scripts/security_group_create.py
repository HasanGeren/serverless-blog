import boto3

# Initialize an EC2 client
ec2_client = boto3.client('ec2')

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
    
# Create a security group
