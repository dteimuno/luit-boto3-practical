import boto3

ec2 = boto3.client('ec2')

response = ec2.create_vpc(
    CidrBlock='10.10.0.0/16',
)

print(response)
for vpc in response["Vpc"]:
    print(vpc["VpcId"], vpc["CidrBlock"], vpc["State"])