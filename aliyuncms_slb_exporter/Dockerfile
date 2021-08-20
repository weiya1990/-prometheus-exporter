FROM python:3.8.11-alpine as base
MAINTAINER weiya 1830624909@qq.com
RUN apk --no-cache add curl 
FROM python:3.8.11-buster  as build
RUN pip install aliyunsdkcore aliyun-python-sdk-core prometheus_client
WORKDIR /opt
FROM base as final
WORKDIR /opt
COPY --from=build  /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
ADD start.py start.py
EXPOSE 8005
CMD ["python", "start.py"]

