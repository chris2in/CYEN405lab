"""
Lab4 Q2c : upload files to an amazon s3 bucket

"""
import boto3

            
s3_client = boto3.client('s3')
filename = 'README.md'

bucket_name = 'yli027lab42bucket'
s3_client.upload_file(filename,bucket_name,filename)
