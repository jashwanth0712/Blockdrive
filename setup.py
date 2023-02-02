import os
from tqdm import tqdm
import subprocess
import time

def loading(t):
    for i in tqdm(range(t)):
        time.sleep(0.01)  # simulate some work


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


