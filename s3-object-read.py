import boto3
Bucket = "S3-Read-Write"
key = "s3-test-object.csv"
s3 = boto3.client('s3')

Bucket="S3-Read-Write"
key="s3-test-object.csv"
result = s3.get_object(Bucket=Bucket, Key=key)
text1 = result["Body"].read().decode('utf-8')
print(text1)
#list00=text.split('\n')
#print(list00[4:10])