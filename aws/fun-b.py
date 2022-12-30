import json
import time
import boto3
import io

def lambda_handler(event, context):
    bucket_arn="arn:aws:s3:::lumine-data-bucket"#define your s3 arn here

    input_size=event['input_size']
    ret={}
    ret['input_size']=input_size
    if input_size<=256000:
        #gateway
        ret["recv_data_len"]=len(event['payload_data'])
    else:
        #s3
        s3 = boto3.client('s3')
        s3 = boto3.resource('s3')
        bucket = bucket_arn.split(':')[-1]
        key=event['payload_data']
        directory = "/tmp/{}".format(key)
        s3.Bucket(bucket).download_file(key, directory)
        ret["recv_data_len"]=os.path.getsize(directory)

        os.popen("rm -rf /tmp")
    ret['t2']=time.time()
    ret['t1']=event['t1']
    return ret
