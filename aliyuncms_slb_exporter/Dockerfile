FROM python:3.8.11-buster 
RUN pip install aliyunsdkcore aliyun-python-sdk-core prometheus_client
WORKDIR /opt
ADD start.py start.py
EXPOSE 8005
CMD ["python", "start.py"]
