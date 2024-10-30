import boto3
ec2 = boto3.client('ec2')
response = ec2.delete_vpc(VpcId='vpc-0d0072fb36de40c39')

print(response)
