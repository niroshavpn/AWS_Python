import boto3


# Create an S3 client
s3 = boto3.client('s3')

filename = '/Users/suresh/Documents/NIROSHA/AWS/Practice/s3-test-object.csv'
filename1 = 's3-test-object.csv'

bucket_name = 'S3-Read-Write'
s3.upload_file(filename, bucket_name, filename1)
