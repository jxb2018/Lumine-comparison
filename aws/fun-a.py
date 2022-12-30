import json
import time
import boto3
import io
def lambda_handler(event, context):
    bucket_arn="arn:aws:s3:::lumine-data-bucket"#define your s3 arn here
    
    ret={}
    input_size=int(event['input_size'])
    ret['input_size']=input_size
    payload_data = str(bytes().zfill(input_size),encoding="utf-8")
    
    t1=time.time()
    ret['t1']=t1

    if input_size<=256000:
        #gateway
        ret['payload_data']=payload_data
    else:
        #s3
        s3 = boto3.client('s3')
        s3 = boto3.resource('s3')
        bucket = bucket_arn.split(':')[-1]
        key=str(int(round(time.time() * 1000)))
        s3.Bucket(bucket).put_object(Key=key, Body=payload_data)
        ret['payload_data']=key

    return ret