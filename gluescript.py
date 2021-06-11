import csv
from botocore.vendored import requests
import boto3
bucket_name = 'cognitocheck'
s3 = s3 = boto3.resource('s3')

bucket = s3.Bucket(bucket_name)

url_lists = [
    'https://raw.githubusercontent.com/ravibalar/Assignment3EBS/master/household_power_consumption.csv']

for url in url_lists:
    session = requests.Session()
    raw_data = session.get(url)
    key = url.split('/')[::-1][0].lower()
    decoded_content = raw_data.content.decode('utf-8')
    print("\n Uploading \n", key)
    bucket.put_object(Key=key, Body=decoded_content, ACL='public-read')
    print("\n Uploaded \n", key)
