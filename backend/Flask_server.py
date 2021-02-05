from flask import Flask, request, jsonify
from datetime import datetime
import sys
import subprocess
import os
import json
import ast
import random

from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)

# @app.after_request
# def after_request(response):
#   response.headers.add('Access-Control-Allow-Origin', '*')
#   response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#   response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#   return response

@app.route("/")    # http://127.0.0.1:8080/  capturing the request
def index():       # This is the response
    cmd="python main.py 20 200"
    subprocess.Popen(cmd)
    return ("Auto Messages generating....")

@app.route("/today")    # http://127.0.0.1:8080/today  capturing the request
def today():       # This is the response
    dt = datetime.now()
    format = "%A, %D %B, %Y %I:%M:%S %p"
    respstr = '<div style="background-color:Violet"><h1>' + dt.strftime(format) + '</h1></div>'
    return ( respstr )

@app.route("/auto-generate",methods=['POST'])   
def generate():       # This is the response
    # print(request.data)
    json_data = request.json
    num = str(json_data['msgs'])
    anomaly= str(json_data['anomaly'])
    cmd="python main.py "+anomaly+" "+num
    # print(cmd)
    p=subprocess.Popen(cmd)
    # print(p.pid)
    pid=p.pid
    return jsonify({"status":"started","process_id":pid})

@app.route("/auto-stop",methods=['POST'])    
def stop():       # This is the response
    # print(request.data)
    json_data = request.json
    # print(json_data)
    pid = json_data['pid']
    try:
        cmd="Taskkill /PID "+str(pid)+" /F"
        # print(cmd)
        output=subprocess.getoutput(cmd)
        return jsonify({"status":"stopped","message": output})
    except:
        return jsonify({"status":Exception})

    
@app.route("/manual-generate",methods=['POST'])   
def manual_generate():       # This is the response
    json_data = request.data
    msgstr=json_data.decode('utf-8')
    filename= "param_"+str(random.randint(0,65365))+str(random.randint(0,65365))+".json"
    with open(filename, "w") as tmpfile:
        tmpfile.write(msgstr+"\n")
        print(filename)
    cmd="python manual_message.py "+filename
    print(subprocess.getoutput(cmd))
    with open("manualmessage.json", "r") as tmpfile:
        msg=tmpfile.read()
    return jsonify({"status":"started", "result": msg})       


if __name__ == "__main__":
    app.run()
