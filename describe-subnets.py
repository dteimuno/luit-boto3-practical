import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_subnets(
    Filters=[
        {
            'Name': 'vpc-id',
            'Values': [
                'vpc-0db48b8b5c3211888',
            ],
        },
    ],
)

print(response)

for subnet in response["Subnets"]:
    print(subnet["AvailabilityZoneId"], subnet["CidrBlock"], subnet["VpcId"] )