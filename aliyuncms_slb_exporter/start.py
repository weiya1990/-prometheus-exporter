#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from aliyunsdkcore.auth.credentials import AccessKeyCredential
from aliyunsdkcore.auth.credentials import StsTokenCredential
import json
import socket
from prometheus_client import Gauge,start_http_server
from time import sleep
import os
#获取系统的环境变量，并传递给python变量
env_dist = os.environ
MetricName_list = env_dist.get('MetricName_list').split(',')
slb_region = env_dist.get('slb_region')
slb_domain = env_dist.get('slb_domain')
slb_instance_list = env_dist.get('slb_instance_list').split(',')
slb_port_list = env_dist.get('slb_port_list').split(',')
interval = env_dist.get('interval') #获取监控时间间隔
aliyun_ak = env_dist.get('aliyun_ak')
aliyun_sk = env_dist.get('aliyun_sk')


def get_request():
    for metricname in MetricName_list:
        client = AcsClient(region_id=slb_region, credential=credentials)
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain(slb_domain)
        request.set_method('POST')
        request.set_protocol_type('https') # https | http
        request.set_version('2019-01-01')
        request.set_action_name('DescribeMetricList')
        request.add_query_param('Namespace', "acs_slb_dashboard")
        request.add_query_param('MetricName', metricname)
        request.add_query_param('Length', "1")
        request.add_query_param('Dimensions', {"instanceId":slb_instance , "port":slb_port})
        response = client.do_action(request)
        #print(str(response, encoding = 'utf-8'))
        #return response
        data = eval(json.loads(str(response, encoding='utf-8'))["Datapoints"])[0]
        #print(data)
        slb_monitor_Maximum.labels(MetricName=metricname, instance=data['instanceId'], port=data['port'], vip=data['vip']).set(data['Maximum'])
        slb_monitor_Minimum.labels(MetricName=metricname, instance=data['instanceId'], port=data['port'], vip=data['vip']).set(data['Minimum'])
        slb_monitor_Average.labels(MetricName=metricname, instance=data['instanceId'], port=data['port'], vip=data['vip']).set(data['Average'])
if __name__ == '__main__':
    start_http_server(8005)
    credentials = AccessKeyCredential(aliyun_ak, aliyun_sk)
    slb_monitor_Maximum = Gauge('metrics_Maximum', 'Description of gauge', ['MetricName', 'instance', 'port', 'vip'])
    slb_monitor_Minimum = Gauge('metrics_Minimum', 'Description of gauge', ['MetricName', 'instance', 'port', 'vip'])
    slb_monitor_Average = Gauge('metrics_Average', 'Description of gauge', ['MetricName', 'instance', 'port', 'vip'])
    while True:
        for slb_port in slb_port_list:
            for slb_instance in slb_instance_list:
                get_request()
        sleep(int(interval))



    
