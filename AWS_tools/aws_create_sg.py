import subprocess
import sys

### セキュリティグループ作成用変数
sg_name = "test"
vpc_id = "vpc-0445de4659d0116cd"
des = "test_sg"
port_id = ["22", "80"]
ip_add = ["223.218.160.243/32", "0.0.0.0/0"]

err_c = 1


### セキュリティグループ作成
cmd_sg = "aws ec2 create-security-group --group-name " + sg_name + " --vpc-id " + vpc_id + " --description " + des + " --output text"
try:
    group_id = subprocess.check_output(cmd_sg, shell=True)
except subprocess.CalledProcessError as e:
    sys.exit(err_c)

### 作成したセキュリティグループのインバウント設定
i = 0
for id_list in port_id:
    cmd_sg_in = "aws ec2 authorize-security-group-ingress --group-id " + group_id.decode('sjis').strip() \
    + " --protocol tcp --port " + id_list + " --cidr " + ip_add[i]
    subprocess.run(cmd_sg_in, shell=True)
    i = i + 1
print (group_id.decode('sjis').strip())
