"""
Lab 4 Q1H:get info about security group 

"""

import boto3

from botocore.exceptions import ClientError


ec2= boto3.client('ec2')
try:
    response = ec2.describe_security_groups(GroupIds = ["sg-083a2da55f2f92e49"])
    print("success ",response)
except ClientError as e:
    print(e)
    
