import subprocess

cmd = "aws ec2 describe-regions --output table"

subprocess.run(cmd, shell=True)
