

import boto3       # importing boto3 module 
import uuid        # importing uuid module

s3=boto3.client('s3')


# Here defining a function which will genrate a Unique id 
# The genrated bucket name must be 3 to 64 chractor

def object_uuid(object_prefix):
    return ''.join([object_prefix, str(uuid.uuid4())])

# s3.upload_file('FILE_NAME', 'BUCKET_NAME', 'OBJECT_NAME')
s3.upload_file(r'/home/arvind/Desktop/Document.docx', 'unir-test', object_uuid('MY_Document.docx'))

