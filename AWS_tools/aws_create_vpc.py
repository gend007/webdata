import subprocess
import sys

### 共通変数
err_c = 1

### VPC作成用変数
cidr_ip = "10.123.40.0/24"
subnet_ip = "10.123.40.0/28"
dist_ip = "0.0.0.0/0"



### VPC作成
cmd_vpc = "aws ec2 create-vpc --cidr-block " + cidr_ip +  ' --query "Vpc.VpcId"'
try:
    vpc_id = subprocess.check_output(cmd_vpc, shell=True)
    vpc_id = vpc_id.decode('sjis').strip()
except subprocess.CalledProcessError as e:
    sys.exit(err_c)


### サブネットの作成
cmd_subnet = "aws ec2 create-subnet --vpc-id " + vpc_id + " --cidr-block " + subnet_ip + \
              ' --query "Subnet.SubnetId"'
try:
    subunet_id = subprocess.check_output(cmd_subnet, shell=True)
    subunet_id = subunet_id.decode('sjis').strip()
except subprocess.CalledProcessError as e:
    sys.exit(err_c)


### インターネットゲートウェイ作成
cmd_gw = "aws ec2 create-internet-gateway " '--query "InternetGateway.InternetGatewayId"'
try:
    gw_id = subprocess.check_output(cmd_gw, shell=True)
    gw_id = gw_id.decode('sjis').strip()
except subprocess.CalledProcessError as e:
    sys.exit(err_c)


### VPCへのアタッチ
cmd_vpc_map = "aws ec2 attach-internet-gateway --internet-gateway-id " + gw_id + " --vpc-id " + vpc_id
rc = subprocess.run(cmd_vpc_map, shell=True)
if rc == err_c:
    sys.exit(err_c)


### ルートテーブル作成
cmd_rt = "aws ec2 create-route-table --vpc-id " + vpc_id + ' --query "RouteTable.RouteTableId"'
try:
    rt_id = subprocess.check_output(cmd_rt, shell=True)
    rt_id = rt_id.decode('sjis').strip()
except subprocess.CalledProcessError as e:
    sys.exit(err_c)


### ルートの作成
cmd_root = "aws ec2 create-route --route-table-id " + rt_id + " --destination-cidr-block "\
            + dist_ip + " --gateway-id " + gw_id
rc = subprocess.run(cmd_root, shell=True, stdout=subprocess.DEVNULL)
if rc == err_c:
    sys.exit(err_c)


### ルートテーブルへのマッピング
cmd_rt_map = "aws ec2 associate-route-table --route-table-id " + rt_id + " --subnet-id " + subunet_id
rc = subprocess.run(cmd_rt_map, shell=True, stdout=subprocess.DEVNULL)
if rc == err_c:
    sys.exit(err_c)
