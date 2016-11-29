import paramiko
import time
from flask import Flask,render_template
from flask import request
import xml.etree.cElementTree as ET
import requests
import json
from flask.json import jsonify

node1="Test1"

topologyData01 ={
    "nodes": [
        {"id": 0, "x": 410, "y": 100, "name": node1},
        {"id": 1, "x": 410, "y": 300, "name": "12K-2"},
        {"id": 2, "x": 660, "y": 280, "name": "Of-9k-03"},
        {"id": 3, "x": 660, "y": 100, "name": "Of-9k-02"},
        {"id": 4, "x": 180, "y": 190, "name": "Of-9k-01"}
    ],
    "links": [
        {"source": 0, "target": 1},
        {"source": 1, "target": 2},
        {"source": 1, "target": 3},
        {"source": 4, "target": 1},
        {"source": 2, "target": 3},
        {"source": 2, "target": 0},
        {"source": 3, "target": 0},
        {"source": 3, "target": 0},
        {"source": 3, "target": 0},
        {"source": 0, "target": 4},
        {"source": 0, "target": 4},
        {"source": 0, "target": 3}
    ]
};


raw_topology={
  "version": "string",
  "response": {
    "nodes": [
      {
        "family": "1",
        "greyOut": "true",
        "ip": "string",
        "userId": "string",
        "aclApplied": "true",
        "osType": "string",
        "id": "1",
        "roleSource": "string",
        "label": "1",
        "upperNode": "2",
        "deviceType": "router",
        "platformId": "1",
        "role": "string",
        "nodeType": "1",
        "tags": [
          "1"
        ],
        "vlanId": "string",
        "networkType": "string",
        "customParam": {
          "y": 0,
          "x": 0,
          "parentNodeId": "string",
          "id": "string",
          "label": "string"
        },
        "softwareVersion": "string",
        "y": 0,
        "x": 0,
        "fixed": "true",
        "dataPathId": "string",
        "order": 0
      }
    ],
    "id": "1",
    "links": [
      {
        "endPortID": "1",
        "startPortName": "1",
        "endPortIpv4Address": "1",
        "startPortID": "string",
        "greyOut": "true",
        "endPortName": "1",
        "endPortIpv4Mask": "string",
        "id": "1",
        "source": "1",
        "tag": "1",
        "startPortSpeed": "string",
        "startPortIpv4Address": "string",
        "endPortSpeed": "string",
        "linkStatus": "string",
        "startPortIpv4Mask": "string",
        "target": "1"
      }
    ]
  }
}

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    #return '<h1>Home</h1>'
    text='''Alex_Controller '''
    print text
    return render_template('index.html',text=text)

@app.route('/data', methods=['GET', 'POST'])
def data():
    #return '<h1>Home</h1>'
    text='''Alex_Controller '''
    print text
    node_name="Alex1111"
    return  jsonify(topologyData01)

if __name__ == '__main__':
    

    app.run(host="127.0.0.1", port=int("7778"))