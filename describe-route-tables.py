import boto3
ec2 = boto3.client('ec2')

response = ec2.describe_route_tables()

print(response)

