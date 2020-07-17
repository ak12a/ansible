import boto3

s3 = boto3.client('s3')

             # 'FileDirectory', 'bucketname', 'objectname'
s3.upload_file(r'/home/arvind/Desktop/doc.zip','unir-test','kumar.zip')
