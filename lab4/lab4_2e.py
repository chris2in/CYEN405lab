"""
Lab4 Q2e : create presigned URLs

"""
import boto3
#import requests
import logging 
         
bucket_name = 'yli027lab42bucket'  

key = 'README.md'
s3= boto3.client('s3')
response = s3.generate_presigned_url(ClientMethod = 'get_object',Params={
    'Bucket':bucket_name,
    'Key':key
})
print(response)

