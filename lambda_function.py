import boto3
import requests
from botocore.exceptions import ClientError
import logging
import pandas as pd

# Download URL
url = 'https://www.arcgis.com/sharing/rest/content/items/e5fd11150d274bebaaf8fe2a7a2bda11/data'
bucket_name = ""

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def lambda_handler(event, context):
    myfile = requests.get(url, allow_redirects=True)
    with open('/tmp/cov_data.xlsx', 'wb') as f:
        f.write(myfile.content)
    data_xls = pd.read_excel('/tmp/cov_data.xlsx')
    data_xls = data_xls.to_csv('/tmp/cov_data.csv',encoding='utf-8')
    upload_file('/tmp/cov_data.csv', bucket_name, "cov_data.csv")
