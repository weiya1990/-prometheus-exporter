## 获取阿里云SLB监控指标使用手册
### 安装方式使用docker或者本地
启动需要传入变量
- MetricName_list 监控指标 "ActiveConnection,TrafficTXNew,TrafficRXNew,DropPacketRX"
- aliyun_ak AK验证
- aliyun_sk SK验证 
- slb_instance 负载均衡实例ID"id_xxxx"
- slb_port_list 需要监控的端口"80,443"
- slb_region 实例所在地区"cn-shanghai"
- slb_domain 监控api地址"metrics.cn-shanghai.aliyuncs.com"
- interval 获取监控数据间隔时间
#### docker启动实例
```bash
#制作镜像
docker build -t aliyuncms_slb_exporter:v1 .
#使用-e参数传递系统变量
docker run -it --name aliyuncms_slb_exporter -p 8005:8005 -e MetricName_list="ActiveConnection,TrafficTXNew,TrafficRXNew,DropPacketRX" -e slb_region="cn-shanghai" -e slb_domain="metrics.cn-shanghai.aliyuncs.com" -e slb_instance_list="lb-uf6ho44td7800wv67bf4z,lb-uf69y1jrgv3pcasuum6ql" -e slb_port_list="80,443" -e aliyun_ak="xxxx" -e aliyun_sk="xxxx" -e interval=10  aliyuncms_slb_exporter:v1 
```
#### 本地python包启动
```bash
#定义环境变量
export MetricName_list="ActiveConnection,TrafficTXNew,TrafficRXNew,DropPacketRX"
export slb_region="cn-shanghai"
export slb_domain="metrics.cn-shanghai.aliyuncs.com"
export slb_instance_list="lb-uf6ho44td7800wv67bf4z,lb-uf69y1jrgv3pcasuum6ql"
export slb_port_list="80,443"
export aliyun_ak="xxx"
export aliyun_sk="xxx"
export interval=10
#启动命令
python start.py
```
#### k8s部署
```bash
kubectl apply -f k8s/deploy.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/servicemonitor.yaml
```

