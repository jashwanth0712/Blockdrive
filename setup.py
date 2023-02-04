import os
from tqdm import tqdm
import subprocess 
import time
import sys
import win32com.client

#------------------function for loading animation-----------------
def loading(t):
    for i in tqdm(range(t), desc="creating... ", ncols=80, bar_format="{l_bar}{bar}"):
        time.sleep(0.01)
#------------------pin to quick access------------------
def pin_to_quick_access(folder_path):
    shell = win32com.client.Dispatch("WScript.Shell")
    folder_path = os.path.abspath(folder_path)
    folder = shell.NameSpace(folder_path)
    folder.self.Path.Verbs().Item("Pin to Quick access").DoIt()
#--------------------function to run shell commands-----------
def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, encoding='utf-8')
    return result.stdout
#-----------------------setup code----------------------
version=run_command(" @lighthouse-web3/sdk --version")
if(version ==""):
    print("[ ] installing lighthouse")
    print(run_command("npm i -g @lighthouse-web3/sdk"))

folder_name = "Blockdrive"
drive = os.path.expanduser("~")  # uses the home directory of the current user
path = os.path.join(drive, folder_name)
if not os.path.exists(path):
    loading(100)
    print("[ ] created blockdrive folder")
    os.makedirs(path)

else:
    print("[ ] blockdrive folder already existing")
subprocess.call(["python", "python_files/watcher.py"])


