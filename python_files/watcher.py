import time
import os
import subprocess
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
        folder_name = "Blockdrive"
        drive = os.path.expanduser("~")  # uses the home directory of the current user
        path = os.path.join(drive, folder_name)
        event_handler = LoggingEventHandler()
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)
        print("[ ] observing ",path)
        observer.start()
        try:
            while True:
                time.sleep(1)
        finally:
            observer.stop()
            observer.join()
    except Exception:
        print("[\033[31m*\033[0m] Exception occured, trying to run setup.py")
        subprocess.call(["python", "./setup.py"])



