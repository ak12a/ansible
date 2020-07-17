import boto3
import uuid

def create_bucket_name(bucket_prefix):
     # The genrated bucket name must be 3 to 64 chractor
     return ''.join([bucket_prefix, str(uuid.uuid4())])

print(create_bucket_name('test.name'))