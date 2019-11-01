"""
Lab 4 Q1F:create a new key pair

"""

import boto3

ec2= boto3.client('ec2')
response = ec2.create_key_pair(KeyName = "yli027lab41fKey")
print("success ",response)

    
