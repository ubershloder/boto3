import boto3
from botocore.config import Config

uber_config = Config(
                   region_name='us-west-2',
)
session = boto3.session.Session(profile_name="me")

client = session.client('ec2', config=uber_config)
session.client('sts').get_caller_identity().get('Account')


key = client.create_key_pair(
    KeyName='morekeasdy'
)
key['KeyMaterial']

# response = client.run_instances(
#     ImageId='string',
#     DryRun=True,
#     InstanceType='t2.micro',
#     KeyName='string',
# )