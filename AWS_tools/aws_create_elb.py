import subprocess
import sys

### 共通変数
err_c = 1

### ELB作成用変数
elb_name = ""
lsnrs = "Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80"
subnet_id = ""
sg_id = ""
target = "Target=HTTP:80/png,Interval=30,UnhealthyThreshold=2,HealthyThreshold=2,Timeout=3"
instance_id = ""



### ELB作成
cmd_elb = "aws elb create-load-balancer --load-balancer-name " + elb_name +  " --listeners " + lsnrs + \
           " --subnets " + subnet_id + " --security-groups " + sg_id +
try:
    dns_name = subprocess.check_output(cmd_elb, shell=True)
    dns_name = dns_name.decode('sjis').strip()
    print("DNS名: " + dns_name)
except subprocess.CalledProcessError as e:
    sys.exit(err_c)


### ヘルスチェック設定
cmd_hc = "aws elb configure-health-check --load-balancer-name " + elb_name + " --health-check " +  target
rc = subprocess.run(cmd_hc, shell=True, stdout=subprocess.DEVNULL)
if rc == err_c:
    sys.exit(err_c)


### ELBへインスタンス割り当て
cmd_elb_map = "aws elb register-instances-with-load-balancer --load-balancer-name " + elb_name + \ 
              " --instances " + instance_id
rc = subprocess.run(cmd_elb_map, shell=True, stdout=subprocess.DEVNULL)
if rc == err_c:
    sys.exit(err_c)



print("success!!  Create ELB")