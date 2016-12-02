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


topologyData02={
    "nodes": [
        {"id": 0, "x": 410, "y": 100, "name": "12K-1"},
        {"id": 1, "x": 410, "y": 280, "name": "12K-2"},
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
        {"source": 0, "target": 4},
        {"source": 0, "target": 3},
        {"source": 0, "target": 3},
        {"source": 0, "target": 3},
        {"source": 0, "target": 3},
        {"source": 0, "target": 3},
        {"source": 0, "target": 3},
        {"source": 0, "target": 3},
        {"source": 0, "target": 3},
        {"source": 0, "target": 3},
        {"source": 0, "target": 3},
        {"source": 0, "target": 3}
    ],
    "nodeSet": [
        {"id": 5, "type": 'nodeSet', "nodes": [2, 3], "root": '2', "x": 660, "y": 190, "name": "Node set 1", "iconType": 'router'},
        {"id": 6, "type": 'nodeSet', "nodes": [1, 5], "root": '1', "x": 410, "y": 190, "name": "Node set 2", "iconType": 'groupS'},
        {"id": 7, "type": 'nodeSet', "nodes": [6, 0], "root": '0', "x": 410, "y": 280, "name": "Node set 3", "iconType": 'groupM'},
        {"id": 8, "type": 'nodeSet', "nodes": [7, 4], "root": '4', "x": 410, "y": 280, "name": "Node set 4", "iconType": 'groupL'}
    ]
};

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    #return '<h1>Home</h1>'
    text='''Home index page '''
    print text
    return render_template('index.html',text=text)

@app.route('/data', methods=['GET', 'POST'])
def data():
    #return '<h1>Home</h1>'
    text='''Jason REST API provides data'''
    print text
    node_name="Alex1111"
    return  jsonify(topologyData02)

if __name__ == '__main__':
    

    app.run(host="127.0.0.1", port=int("7778"))