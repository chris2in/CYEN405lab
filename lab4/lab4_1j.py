"""
Lab 4 Q1J:create new security group 

"""

import boto3

from botocore.exceptions import ClientError


ec2= boto3.client('ec2')
try:
    response = ec2.delete_security_group(GroupId = "sg-0772ca08d0b3252a6")
    print("success ",response)
except ClientError as e:
    print(e)
    
