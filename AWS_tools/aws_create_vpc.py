import subprocess
import sys

### 共通変数
err_c = 1

### VPC作成用変数
cidr_ip = "10.123.40.1/28"
dist_ip = "0.0.0.0/0"


### VPC作成
cmd_vpc = "aws ec2 create-vpc --cidr-block " + cidr_ip +  ' --query "Vpc.VpcId"'
try:
    vpc_id = subprocess.check_output(cmd_vpc, shell=True)
    vpc_id = vpc_id.decode('sjis').strip()
except subprocess.CalledProcessError as e:
    sys.exit(err_c)

### サブネットの作成
