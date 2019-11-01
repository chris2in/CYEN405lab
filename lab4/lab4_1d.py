"""
Lab 4 Q1D: reboot amazon ect instance

"""
import sys
import boto3
from botocore.exceptions import ClientError


ec2= boto3.client('ec2')


    # Do a dryrun first to verify permission 
try:
    # instanceid is one of the stopped instance created earlier 
    ec2.reboot_instances(InstanceIds=['i-051a3a0226060ed45'],DryRun = True)
except ClientError as e:
    if'DryRunOperation' not in str(e):
        print("You dont have the permission to reboot instances ")
        raise 
#Dry run succeeded, run reboot_instances again without dryrun 
try:
    # instanceid is one of the stopped instance created earlier 
    response = ec2.reboot_instances(InstanceIds=['i-051a3a0226060ed45'],DryRun =False)
    print("success ",response)
except ClientError as e:
    print("error ", e)
    
