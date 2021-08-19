import boto3
client = boto3.client('s3')
location = {'LocationConstraint': 'us-west-2'} #declare location to overide default
client.create_bucket(Bucket = 'awuks', CreateBucketConfiguration = location) #create bucket
#check for existing buckets
response = client.list_buckets()
print(response)
