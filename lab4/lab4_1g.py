"""
Lab 4 Q1G:delete a new key pair

"""

import boto3

ec2= boto3.client('ec2')
response = ec2.delete_key_pair(KeyName = "yli027lab41fKey")
print("success ",response)

    
