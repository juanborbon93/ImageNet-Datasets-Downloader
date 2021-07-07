import boto3
import os
from botocore.exceptions import ClientError
import logging
from tqdm import tqdm
from multiprocessing import Pool


bucket = "ilox-ml-data"
root_dir = 'beltid/other_images'
def upload_file(input):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    file_name, bucket, object_name = input
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

uploads = list()
for root, dirs, files in os.walk("data", topdown=False):
    for file_name in files:
        if file_name.lower().endswith('.jpg'):
            file_path = os.path.join(root, file_name) 
            s3_path = os.path.join(root_dir,file_name)
            uploads.append((file_path,bucket,s3_path))

pool = Pool(processes=4)
result_list_tqdm = []
for result in tqdm(pool.imap(func=upload_file, iterable=uploads), total=len(uploads)):
    result_list_tqdm.append(result)

