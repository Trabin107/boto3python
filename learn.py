import boto3

# Initialize a session using Amazon S3
client = boto3.client('s3', region_name='us-east-1')

# List all buckets
response = client.list_buckets()

# Print bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')