import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_vpcs()
print(response)

for vpc in response["Vpcs"]:
    print(vpc["OwnerId"])