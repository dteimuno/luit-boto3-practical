import boto3

ec2 = boto3.client('ec2')
response = ec2.create_security_group(
    Description='DTM security group',
    GroupName='my-boto3-group',
    VpcId='vpc-0db48b8b5c3211888',
)

print(response)
for sub_response in response:
    print(sub_response["GroupId"])