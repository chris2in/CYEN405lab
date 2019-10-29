"""
Lab4 Q2b : list existing  S3 bucket 
Q1A: 
"""
import boto3

            
s3_client = boto3.client('s3')
response = s3_client.list_buckets()
#output the bucket names 
print('Existing buckets: ')
for bucket in response['Buckets']:
    print(f' {bucket["Name"]}')
