import subprocess

cmd = "aws ec2 describe-instances --query Reservations[*].Instances[*].InstanceId"

output = subprocess.check_output(cmd, shell=True)

print (output.decode('sjis'))
