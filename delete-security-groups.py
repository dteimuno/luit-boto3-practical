import boto3

ec2 = boto3.client('ec2')

response = ec2.delete_security_group(
    GroupId='sg-098d997d9eaf34b6d',
)

print(response)