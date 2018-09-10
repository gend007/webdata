import subprocess
import sys

### インスタンス作成用変数
key_name="testkey.pem"
key_path="testkey.pem"
image_id="ami-6b0d5f0d"
sg_id="sg-0cfe1dff9062480cc"
subnet_id="subnet-02306013c1b432019"
ins_type="t2.micro"

err_c = 1

### キーペアの作成
### キーペアの存在確認
cmd_key_ck = 'aws ec2 describe-key-pairs --filters "Name=key-name,Values="' + key_name + ' --query "KeyPairs[0]"'
try:
    ins_key_name = subprocess.check_output(cmd_key_ck, shell=True)
    ins_key_name = ins_key_name.decode('sjis').strip()

    if ins_key_name == "null":
        cmd_key = "aws ec2 create-key-pair --key-name " + key_name + ' --query "KeyMaterial" --output text > ' + key_path
        subprocess.run(cmd_key, shell=True)
except subprocess.CalledProcessError as e:
    sys.exit(err_c)



### インスタンス作成
cmd_ins = "aws ec2 run-instances --image-id " + image_id + " --security-group-ids " + sg_id + " \
           --subnet-id " + subnet_id + " --associate-public-ip-address --count 1 --instance-type " \
           + ins_type + " --key-name " + key_name + ' --query "Instances[0].InstanceId"'
try:
    ins_id = subprocess.check_output(cmd_ins, shell=True)
    ins_id = ins_id.decode('sjis').strip()
except subprocess.CalledProcessError as e:
    sys.exit(err_c)



### 作成インスタンスのIPアドレス取得
cmd_ip = "aws ec2 describe-instances --instance-ids " + ins_id + ' --query "Reservations[0].Instances[0].PublicIpAddress"'
try:
    cmd_ipadd = subprocess.check_output(cmd_ip, shell=True)
    cmd_ipadd = cmd_ipadd.decode('sjis').strip()
    print(ins_id + " : " + cmd_ipadd)
except subprocess.CalledProcessError as e:
    sys.exit(err_c)
