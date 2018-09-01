import subprocess

sg_name = "test"
vpc_id = "vpc-d1dc8bb6"
des = "test_sg"

port_id = "80"
ip_add = "223.218.160.243/32"


cmd_sg = "aws ec2 create-security-group --group-name " + sg_name + " --vpc-id " + vpc_id + " --description " + des + " --output text"
group_id = subprocess.check_output(cmd_sg, shell=True)
print (group_id.decode('sjis'))


cmd_sg_in = "aws ec2 authorize-security-group-ingress --group-id " + group_id.decode('sjis') + " --protocol tcp --port " + port_id + " --cidr " + ip_add
print(cmd_sg_in)
subprocess.run(cmd_sg_in, shell=True)
