"""
Lab4 Q2a : create an amazon S3 bucket 
Q1A: 
"""
import boto3
import logging 
from botocore.exceptions import ClientError

def create_bucket(bucket_name,region = None):
    try:
        if region is None:
            
            s3_client = boto3.client('s3')
           
            s3_client.create_bucket(Bucket=bucket_name)
            
            #s3.create_bucket(Bucket='mybucket')
        else:
           
            s3_client = boto3.client('s3',region_name = region)
            location = {'LocationConstraint':region}
            s3_client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration = location)
    except ClientError as e : 
        print("ERROR")
        logging.error(e)
        return False 
    return True 

create_bucket('yli027lab42bucket','us-east-2')
