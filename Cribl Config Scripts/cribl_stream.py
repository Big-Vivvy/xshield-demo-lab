import subprocess

def run_command(command, step):
    print(f"Running step {step}: {command}")
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if process.returncode != 0:
        print(f"Failed to execute command: {command}. Error: {error}")
        return False
    print(f"Successfully completed step {step}")
    return True

commands = [
    "sudo apt-get update -y",  # Update package manager
    "sudo apt-get install git -y",  # Install git
    "sudo adduser --disabled-password --gecos '' cribl",  # Add a user named cribl
    "sudo curl -Lso - $(curl https://cdn.cribl.io/dl/latest-x64) | sudo tar zxv -C /opt",  # Download files to /opt directory
    "sudo chown -R cribl:cribl /opt/cribl",  # Change owner of the downloaded files
    "/opt/cribl/bin/cribl boot-start enable -u cribl",  # Start Cribl Stream
    "sudo systemctl daemon-reload",  # Reload the systemd manager configuration
    "sudo systemctl enable cribl",  # Enable Cribl to start at boot
    "sudo systemctl start cribl"  # Start Cribl service
]

for index, command in enumerate(commands, start=1):
    if not run_command(command, index):
        print(f"Aborting due to failure at step {index}")
        break
