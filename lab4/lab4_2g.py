"""
Lab4 Q2f : retrieve a bucket policy
"""
import boto3
bucket_name= 'yli027lab42bucket'
s3= boto3.client('s3')  
response = s3.get_bucket_acl(Bucket=bucket_name)
print(response)

