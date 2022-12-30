import json
import time

def lambda_handler(event, context):
    t1=event['t1']
    t2=event['t2']
    t3=time.time()
    ret={}
    ret['t1-t3']=t3-t1
    ret['t2-t3']=t3-t2
    ret['t1-t2']=t2-t1
    ret['recv_data_len']=event['recv_data_len']
    return ret