"""
Lab4 Q2D : download files from an amazon s3 bucket

"""
import boto3
import botocore
            
s3= boto3.resource('s3')
filename = 'myREADME.md'

bucket_name = 'yli027lab42bucket'
key = 'README.md'
s3.Bucket(bucket_name).download_file(key,filename)
