import os
import time
folder_name = "Blockdrive"
drive = os.path.expanduser("~")  # uses the home directory of the current user
folder_to_watch = os.path.join(drive, folder_name)
before = dict ([(f, None) for f in os.listdir (folder_to_watch)])

def Upload_file(file_name):
  CID=""
  return CID

while 1:
  time.sleep (1)
  after = dict ([(f, None) for f in os.listdir (folder_to_watch)])
  added = [f for f in after if not f in before]
  if added:
    print("Added: ", ", ".join (added))
  before = after
