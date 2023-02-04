import subprocess

def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, encoding='utf-8')
    return result.stdout

command = input("Enter the command to run: ")
output = run_command("npm i -g @lighthouse-web3/sdk")
print("output is ",output)