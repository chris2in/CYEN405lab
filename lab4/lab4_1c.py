"""
Lab 4 Q1B: Start and Stop an amazon ec2 instance

"""
import sys
import boto3
from botocore.exceptions import ClientError


ec2= boto3.client('ec2')

action = sys.argv[1].upper()
if action =='ON':
    # Do a dryrun first to verify permission 
    try:
        # instanceid is one of the stopped instance created earlier 
        ec2.start_instances(InstanceIds=['i-051a3a0226060ed45'],DryRun = True)
    except ClientError as e:
        if'DryRunOperation' not in str(e):
            raise 
    #Dry run succeeded, run start_instances again without dryrun 
    try:
        # instanceid is one of the stopped instance created earlier 
        response = ec2.start_instances(InstanceIds=['i-051a3a0226060ed45'],DryRun =False)
        print(response)
    except ClientError as e:
        print(e)
else:
   # Do a dryrun first to verify permission 
    try:
        # instanceid is one of the stopped instance created earlier 
        ec2.stop_instances(InstanceIds=['i-051a3a0226060ed45'],DryRun = True)
    except ClientError as e:
        if'DryRunOperation' not in str(e):
            raise 
    #Dry run succeeded, run start_instances again without dryrun 
    try:
        # instanceid is one of the stopped instance created earlier 
        response = ec2.stop_instances(InstanceIds=['i-051a3a0226060ed45'],DryRun =False)
        print(response)
    except ClientError as e:
        print(e)

