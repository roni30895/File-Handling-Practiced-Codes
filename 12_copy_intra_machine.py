#Write a function to copy data from one machine to another machine.
import paramiko
import os

def copy_files_over_sftp(host, username, password, src_dir, dest_dir):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)

    sftp = ssh.open_sftp()
    for filename in os.listdir(src_dir):
        src_file = os.path.join(src_dir, "questions.txt")
        dest_file = os.path.join(dest_dir, "questions.txt")
        sftp.put(src_file, dest_file)

    sftp.close()
    ssh.close()

host='ubuntu2004'
username="ubuntu"
password="Rohan@007"
src_dir="F:/Assignment By Rahul/7. File Handling"
dest_dir="/home/ubuntu/copied"
copy_files_over_sftp(host, username, password, src_dir, dest_dir)