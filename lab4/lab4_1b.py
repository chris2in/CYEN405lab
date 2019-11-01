"""
Lab 4 Q1B: Start and Stop Detailed Monitorin of an EC2 instance 

"""
import sys
import boto3
ec2= boto3.client('ec2')
if sys.argv[1] =='ON':
    response = ec2.monitor_instances(InstanceIds=['i-0179c9b4b66e49232'])
else:
    resposne = ec2.unmonitor_instances(InstanceIds=['i-0179c9b4b66e49232'])
print(response)

