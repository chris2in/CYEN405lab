"""
Lab 4 Q1I:create new security group 

"""

import boto3

from botocore.exceptions import ClientError


ec2= boto3.client('ec2')
try:
    response = ec2.create_security_group(GroupName = "lab41I",
                                        Description="lab41I crate 10/29/19")
    print("success ",response)
except ClientError as e:
    print(e)
    
