import boto3

ec2 = boto3.client('ec2')

response = ec2.run_instances(
    ImageId='ami-06b21ccaeff8cd686',
    InstanceType='t2.micro',
    KeyName='keypairforluitccp3',
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        'sg-098d997d9eaf34b6d',
    ]
)

print(response)