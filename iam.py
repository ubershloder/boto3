import boto3
from botocore.config import Config
import random
import string

proxy_definitions = {
    'https': 'https://proxy.amazon.org:2010'
}

my_config = Config(region_name='us-west-2',
                   signature_version='v4',
                   retries={
                       'max_attempts': 10,
                       'mode': 'standard'
                   })
session = boto3.Session(profile_name='me')
session.client('sts').get_caller_identity().get('Account')

# def id_generator(size=10, chars=string.ascii_lowercase):
#     return ''.join(random.choice(chars) for _ in range(size))

# region = "us-east-2"
# bucket_name = "somebucket" + id_generator()
# s3_client = session.client("s3")
# print("Name of bucket is:" + bucket_name)
# location = {'LocationConstraint': region}
# s3_client.create_bucket(
#     Bucket=bucket_name,
#     CreateBucketConfiguration={
#         'LocationConstraint': region
#     },
#     ACL='public-read-write'
# )
