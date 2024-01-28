#+AMDG+#
#MP2 web server application for section 2

import socket
from subprocess import Popen
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/', methods = ["POST", "GET"])
def func():
    if request.method == "POST":
        subprocess.Popen(["python3", "stress_cpu.py"])
        return "Thanks!"
    else:
        sock = socket.gethostbyname()
        print(sock)
        return sock

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
