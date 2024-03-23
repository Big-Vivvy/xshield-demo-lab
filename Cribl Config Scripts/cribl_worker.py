import subprocess
import getpass

def get_input(prompt):
    return getpass.getpass(prompt)

ip_address = get_input("Please enter the IP address of the Cribl Stream Leader for this worker: ")
auth_token = get_input("Please enter the Auth token from the Cribl Stream Leader for this worker: ")

command = f"curl 'http://{ip_address}:9000/init/install-worker.sh?group=default&token={auth_token}&user=cribl&install_dir=%2Fopt%2Fcribl' | bash -"

process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

if process.returncode != 0:
    print(f"Error occurred: {stderr.decode()}")
else:
    print(stdout.decode())
