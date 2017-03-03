'''
Created on Jan 21, 2017

@author: AlexFeng
'''


import paramiko
import time
from flask import Flask,render_template
from flask import request
import xml.etree.cElementTree as ET
import requests
import json
from flask.json import jsonify
from scipy.optimize._tstutils import methods
import copy  
import base64
import random



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

topologyData03={
    "nodes": [
        {"id": 0,"name": "12K-1"},
        {"id": 1,"name": "12K-2"},
        {"id": 2,"name": "Of-9k-03"},
        {"id": 3,"name": "Of-9k-02"},
        {"id": 4,"name": "Of-9k-01"}
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


Result1='''{
  "bgp-linkstate:linkstate-routes": {
    "linkstate-route": [
      {
        "route-key": "AAMAOwMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABgEIAAEBAQkABR4KAAAU",
        "identifier": 2,
        "advertising-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235526
          }
        },
        "prefix-descriptors": {
          "ospf-route-type": "intra-area",
          "ip-reachability-information": "10.0.0.20/30"
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "prefix-attributes": {
            "prefix-metric": 1
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAMAOwMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABQEIAAEBAQkABSDAqAAF",
        "identifier": 2,
        "advertising-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235525
          }
        },
        "prefix-descriptors": {
          "ospf-route-type": "intra-area",
          "ip-reachability-information": "192.168.0.5/32"
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "prefix-attributes": {
            "prefix-metric": 1
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAIAYQMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgAAgEBACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABgEDAAQKAAAJAQQABAoAAAo=",
        "identifier": 2,
        "local-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235522
          }
        },
        "link-descriptors": {
          "ipv4-neighbor-address": "10.0.0.10",
          "ipv4-interface-address": "10.0.0.9"
        },
        "remote-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235526
          }
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "link-attributes": {
            "remote-ipv4-router-id": "192.168.0.6",
            "max-link-bandwidth": "TO5rKA==",
            "te-metric": 1,
            "max-reservable-bandwidth": "TO5rKA==",
            "admin-group": 0,
            "metric": 1,
            "local-ipv4-router-id": "192.168.0.2",
            "unreserved-bandwidth": [
              {
                "priority": 2,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 3,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 0,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 1,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 6,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 7,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 4,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 5,
                "bandwidth": "TO5rKA=="
              }
            ]
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAMAOwMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgAAwEIAAEBAQkABR4KAAAM",
        "identifier": 2,
        "advertising-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235523
          }
        },
        "prefix-descriptors": {
          "ospf-route-type": "intra-area",
          "ip-reachability-information": "10.0.0.12/30"
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "prefix-attributes": {
            "prefix-metric": 1
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAMAOwMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABgEIAAEBAQkABR4KAAAY",
        "identifier": 2,
        "advertising-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235526
          }
        },
        "prefix-descriptors": {
          "ospf-route-type": "intra-area",
          "ip-reachability-information": "10.0.0.24/30"
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "prefix-attributes": {
            "prefix-metric": 1
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAMAOwMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgAAgEIAAEBAQkABSACAgIC",
        "identifier": 2,
        "advertising-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235522
          }
        },
        "prefix-descriptors": {
          "ospf-route-type": "intra-area",
          "ip-reachability-information": "2.2.2.2/32"
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "prefix-attributes": {
            "prefix-metric": 1
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAIAYQMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgAAQEBACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgAAwEDAAQKAAAFAQQABAoAAAY=",
        "identifier": 2,
        "local-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235521
          }
        },
        "link-descriptors": {
          "ipv4-neighbor-address": "10.0.0.6",
          "ipv4-interface-address": "10.0.0.5"
        },
        "remote-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235523
          }
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "link-attributes": {
            "remote-ipv4-router-id": "192.168.0.3",
            "max-link-bandwidth": "TO5rKA==",
            "te-metric": 1,
            "max-reservable-bandwidth": "TO5rKA==",
            "admin-group": 0,
            "metric": 1,
            "local-ipv4-router-id": "192.168.0.1",
            "unreserved-bandwidth": [
              {
                "priority": 2,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 3,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 0,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 1,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 6,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 7,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 4,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 5,
                "bandwidth": "TO5rKA=="
              }
            ]
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAIAYQMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABgEBACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABAEDAAQKAAAWAQQABAoAABU=",
        "identifier": 2,
        "local-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235526
          }
        },
        "link-descriptors": {
          "ipv4-neighbor-address": "10.0.0.21",
          "ipv4-interface-address": "10.0.0.22"
        },
        "remote-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235524
          }
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "link-attributes": {
            "remote-ipv4-router-id": "192.168.0.4",
            "max-link-bandwidth": "TO5rKA==",
            "te-metric": 1,
            "max-reservable-bandwidth": "TO5rKA==",
            "admin-group": 0,
            "metric": 1,
            "local-ipv4-router-id": "192.168.0.6",
            "unreserved-bandwidth": [
              {
                "priority": 2,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 3,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 0,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 1,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 6,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 7,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 4,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 5,
                "bandwidth": "TO5rKA=="
              }
            ]
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAIAYQMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABgEBACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgAAgEDAAQKAAAKAQQABAoAAAk=",
        "identifier": 2,
        "local-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235526
          }
        },
        "link-descriptors": {
          "ipv4-neighbor-address": "10.0.0.9",
          "ipv4-interface-address": "10.0.0.10"
        },
        "remote-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235522
          }
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "link-attributes": {
            "remote-ipv4-router-id": "192.168.0.2",
            "max-link-bandwidth": "TO5rKA==",
            "te-metric": 1,
            "max-reservable-bandwidth": "TO5rKA==",
            "admin-group": 0,
            "metric": 1,
            "local-ipv4-router-id": "192.168.0.6",
            "unreserved-bandwidth": [
              {
                "priority": 2,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 3,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 0,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 1,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 6,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 7,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 4,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 5,
                "bandwidth": "TO5rKA=="
              }
            ]
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAMAOwMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgAAwEIAAEBAQkABR4KAAAE",
        "identifier": 2,
        "advertising-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235523
          }
        },
        "prefix-descriptors": {
          "ospf-route-type": "intra-area",
          "ip-reachability-information": "10.0.0.4/30"
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "prefix-attributes": {
            "prefix-metric": 1
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAMAOwMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgAAgEIAAEBAQkABSDAqAAC",
        "identifier": 2,
        "advertising-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235522
          }
        },
        "prefix-descriptors": {
          "ospf-route-type": "intra-area",
          "ip-reachability-information": "192.168.0.2/32"
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "prefix-attributes": {
            "prefix-metric": 1
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAIAYQMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgAAwEBACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgAAQEDAAQKAAAGAQQABAoAAAU=",
        "identifier": 2,
        "local-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235523
          }
        },
        "link-descriptors": {
          "ipv4-neighbor-address": "10.0.0.5",
          "ipv4-interface-address": "10.0.0.6"
        },
        "remote-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235521
          }
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "link-attributes": {
            "remote-ipv4-router-id": "192.168.0.1",
            "max-link-bandwidth": "TO5rKA==",
            "te-metric": 1,
            "max-reservable-bandwidth": "TO5rKA==",
            "admin-group": 0,
            "metric": 1,
            "local-ipv4-router-id": "192.168.0.3",
            "unreserved-bandwidth": [
              {
                "priority": 2,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 3,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 0,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 1,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 6,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 7,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 4,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 5,
                "bandwidth": "TO5rKA=="
              }
            ]
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAMAOwMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgAAQEIAAEBAQkABR4KAAAE",
        "identifier": 2,
        "advertising-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235521
          }
        },
        "prefix-descriptors": {
          "ospf-route-type": "intra-area",
          "ip-reachability-information": "10.0.0.4/30"
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "prefix-attributes": {
            "prefix-metric": 1
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAMAOwMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABgEIAAEBAQkABR4KAAAI",
        "identifier": 2,
        "advertising-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235526
          }
        },
        "prefix-descriptors": {
          "ospf-route-type": "intra-area",
          "ip-reachability-information": "10.0.0.8/30"
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "prefix-attributes": {
            "prefix-metric": 1
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAEALQMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABA==",
        "identifier": 2,
        "node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235524
          }
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "node-attributes": {
            "ipv4-router-id": "192.168.0.4"
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAEALQMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgAAw==",
        "identifier": 2,
        "node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235523
          }
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "node-attributes": {
            "ipv4-router-id": "192.168.0.3"
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAEALQMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABg==",
        "identifier": 2,
        "node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235526
          }
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "node-attributes": {
            "ipv4-router-id": "192.168.0.6"
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAMAOwMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgAAwEIAAEBAQkABR4KAAAQ",
        "identifier": 2,
        "advertising-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235523
          }
        },
        "prefix-descriptors": {
          "ospf-route-type": "intra-area",
          "ip-reachability-information": "10.0.0.16/30"
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "prefix-attributes": {
            "prefix-metric": 1
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAEALQMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABQ==",
        "identifier": 2,
        "node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235525
          }
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "node-attributes": {
            "ipv4-router-id": "192.168.0.5"
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAIAYQMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABQEBACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABgEDAAQKAAAZAQQABAoAABo=",
        "identifier": 2,
        "local-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235525
          }
        },
        "link-descriptors": {
          "ipv4-neighbor-address": "10.0.0.26",
          "ipv4-interface-address": "10.0.0.25"
        },
        "remote-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235526
          }
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "link-attributes": {
            "remote-ipv4-router-id": "192.168.0.6",
            "max-link-bandwidth": "TO5rKA==",
            "te-metric": 1,
            "max-reservable-bandwidth": "TO5rKA==",
            "admin-group": 0,
            "metric": 1,
            "local-ipv4-router-id": "192.168.0.5",
            "unreserved-bandwidth": [
              {
                "priority": 2,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 3,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 0,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 1,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 6,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 7,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 4,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 5,
                "bandwidth": "TO5rKA=="
              }
            ]
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAEALQMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgAAg==",
        "identifier": 2,
        "node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235522
          }
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "node-attributes": {
            "ipv4-router-id": "192.168.0.2"
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAIAYQMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABAEBACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgAAwEDAAQKAAAOAQQABAoAAA0=",
        "identifier": 2,
        "local-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235524
          }
        },
        "link-descriptors": {
          "ipv4-neighbor-address": "10.0.0.13",
          "ipv4-interface-address": "10.0.0.14"
        },
        "remote-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235523
          }
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "link-attributes": {
            "remote-ipv4-router-id": "192.168.0.3",
            "max-link-bandwidth": "TO5rKA==",
            "te-metric": 1,
            "max-reservable-bandwidth": "TO5rKA==",
            "admin-group": 0,
            "metric": 1,
            "local-ipv4-router-id": "192.168.0.4",
            "unreserved-bandwidth": [
              {
                "priority": 2,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 3,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 0,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 1,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 6,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 7,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 4,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 5,
                "bandwidth": "TO5rKA=="
              }
            ]
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAEALQMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgAAQ==",
        "identifier": 2,
        "node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235521
          }
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "node-attributes": {
            "ipv4-router-id": "192.168.0.1"
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAMAOwMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABQEIAAEBAQkABR4KAAAY",
        "identifier": 2,
        "advertising-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235525
          }
        },
        "prefix-descriptors": {
          "ospf-route-type": "intra-area",
          "ip-reachability-information": "10.0.0.24/30"
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "prefix-attributes": {
            "prefix-metric": 1
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAMAOwMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgAAgEIAAEBAQkABR4KAAAI",
        "identifier": 2,
        "advertising-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235522
          }
        },
        "prefix-descriptors": {
          "ospf-route-type": "intra-area",
          "ip-reachability-information": "10.0.0.8/30"
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "prefix-attributes": {
            "prefix-metric": 1
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAMAOwMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgAAQEIAAEBAQkABSABAQEB",
        "identifier": 2,
        "advertising-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235521
          }
        },
        "prefix-descriptors": {
          "ospf-route-type": "intra-area",
          "ip-reachability-information": "1.1.1.1/32"
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "prefix-attributes": {
            "prefix-metric": 1
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAMAOwMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABAEIAAEBAQkABSDAqAAE",
        "identifier": 2,
        "advertising-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235524
          }
        },
        "prefix-descriptors": {
          "ospf-route-type": "intra-area",
          "ip-reachability-information": "192.168.0.4/32"
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "prefix-attributes": {
            "prefix-metric": 1
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAIAYQMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgAAwEBACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABQEDAAQKAAARAQQABAoAABI=",
        "identifier": 2,
        "local-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235523
          }
        },
        "link-descriptors": {
          "ipv4-neighbor-address": "10.0.0.18",
          "ipv4-interface-address": "10.0.0.17"
        },
        "remote-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235525
          }
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "link-attributes": {
            "remote-ipv4-router-id": "192.168.0.5",
            "max-link-bandwidth": "TO5rKA==",
            "te-metric": 1,
            "max-reservable-bandwidth": "TO5rKA==",
            "admin-group": 0,
            "metric": 1,
            "local-ipv4-router-id": "192.168.0.3",
            "unreserved-bandwidth": [
              {
                "priority": 2,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 3,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 0,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 1,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 6,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 7,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 4,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 5,
                "bandwidth": "TO5rKA=="
              }
            ]
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAMAOwMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABgEIAAEBAQkABSDAqAAG",
        "identifier": 2,
        "advertising-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235526
          }
        },
        "prefix-descriptors": {
          "ospf-route-type": "intra-area",
          "ip-reachability-information": "192.168.0.6/32"
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "prefix-attributes": {
            "prefix-metric": 1
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAMAOwMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABAEIAAEBAQkABR4KAAAM",
        "identifier": 2,
        "advertising-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235524
          }
        },
        "prefix-descriptors": {
          "ospf-route-type": "intra-area",
          "ip-reachability-information": "10.0.0.12/30"
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "prefix-attributes": {
            "prefix-metric": 1
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAMAOwMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABQEIAAEBAQkABR4KAAAQ",
        "identifier": 2,
        "advertising-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235525
          }
        },
        "prefix-descriptors": {
          "ospf-route-type": "intra-area",
          "ip-reachability-information": "10.0.0.16/30"
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "prefix-attributes": {
            "prefix-metric": 1
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAIAYQMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABAEBACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABgEDAAQKAAAVAQQABAoAABY=",
        "identifier": 2,
        "local-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235524
          }
        },
        "link-descriptors": {
          "ipv4-neighbor-address": "10.0.0.22",
          "ipv4-interface-address": "10.0.0.21"
        },
        "remote-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235526
          }
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "link-attributes": {
            "remote-ipv4-router-id": "192.168.0.6",
            "max-link-bandwidth": "TO5rKA==",
            "te-metric": 1,
            "max-reservable-bandwidth": "TO5rKA==",
            "admin-group": 0,
            "metric": 1,
            "local-ipv4-router-id": "192.168.0.4",
            "unreserved-bandwidth": [
              {
                "priority": 2,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 3,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 0,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 1,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 6,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 7,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 4,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 5,
                "bandwidth": "TO5rKA=="
              }
            ]
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAMAOgMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABAEIAAEBAQkABBisEAE=",
        "identifier": 2,
        "advertising-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235524
          }
        },
        "prefix-descriptors": {
          "ospf-route-type": "intra-area",
          "ip-reachability-information": "172.16.1.0/24"
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "prefix-attributes": {
            "prefix-metric": 1
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAIAYQMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABQEBACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgAAwEDAAQKAAASAQQABAoAABE=",
        "identifier": 2,
        "local-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235525
          }
        },
        "link-descriptors": {
          "ipv4-neighbor-address": "10.0.0.17",
          "ipv4-interface-address": "10.0.0.18"
        },
        "remote-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235523
          }
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "link-attributes": {
            "remote-ipv4-router-id": "192.168.0.3",
            "max-link-bandwidth": "TO5rKA==",
            "te-metric": 1,
            "max-reservable-bandwidth": "TO5rKA==",
            "admin-group": 0,
            "metric": 1,
            "local-ipv4-router-id": "192.168.0.5",
            "unreserved-bandwidth": [
              {
                "priority": 2,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 3,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 0,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 1,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 6,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 7,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 4,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 5,
                "bandwidth": "TO5rKA=="
              }
            ]
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAMAOwMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABAEIAAEBAQkABR4KAAAU",
        "identifier": 2,
        "advertising-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235524
          }
        },
        "prefix-descriptors": {
          "ospf-route-type": "intra-area",
          "ip-reachability-information": "10.0.0.20/30"
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "prefix-attributes": {
            "prefix-metric": 1
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAIAYQMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgAAwEBACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABAEDAAQKAAANAQQABAoAAA4=",
        "identifier": 2,
        "local-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235523
          }
        },
        "link-descriptors": {
          "ipv4-neighbor-address": "10.0.0.14",
          "ipv4-interface-address": "10.0.0.13"
        },
        "remote-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235524
          }
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "link-attributes": {
            "remote-ipv4-router-id": "192.168.0.4",
            "max-link-bandwidth": "TO5rKA==",
            "te-metric": 1,
            "max-reservable-bandwidth": "TO5rKA==",
            "admin-group": 0,
            "metric": 1,
            "local-ipv4-router-id": "192.168.0.3",
            "unreserved-bandwidth": [
              {
                "priority": 2,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 3,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 0,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 1,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 6,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 7,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 4,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 5,
                "bandwidth": "TO5rKA=="
              }
            ]
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAIAYQMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABgEBACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgABQEDAAQKAAAaAQQABAoAABk=",
        "identifier": 2,
        "local-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235526
          }
        },
        "link-descriptors": {
          "ipv4-neighbor-address": "10.0.0.25",
          "ipv4-interface-address": "10.0.0.26"
        },
        "remote-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235525
          }
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "link-attributes": {
            "remote-ipv4-router-id": "192.168.0.5",
            "max-link-bandwidth": "TO5rKA==",
            "te-metric": 1,
            "max-reservable-bandwidth": "TO5rKA==",
            "admin-group": 0,
            "metric": 1,
            "local-ipv4-router-id": "192.168.0.6",
            "unreserved-bandwidth": [
              {
                "priority": 2,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 3,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 0,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 1,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 6,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 7,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 4,
                "bandwidth": "TO5rKA=="
              },
              {
                "priority": 5,
                "bandwidth": "TO5rKA=="
              }
            ]
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAMAOwMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgAAwEIAAEBAQkABSDAqAAD",
        "identifier": 2,
        "advertising-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235523
          }
        },
        "prefix-descriptors": {
          "ospf-route-type": "intra-area",
          "ip-reachability-information": "192.168.0.3/32"
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "prefix-attributes": {
            "prefix-metric": 1
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      },
      {
        "route-key": "AAMAOwMAAAAAAAAAAgEAACACAAAEAAAAAQIBAATAqAAEAgIABAAAAAACAwAEwKgAAQEIAAEBAQkABSDAqAAB",
        "identifier": 2,
        "advertising-node-descriptors": {
          "area-id": 0,
          "as-number": 1,
          "domain-id": 3232235524,
          "ospf-node": {
            "ospf-router-id": 3232235521
          }
        },
        "prefix-descriptors": {
          "ospf-route-type": "intra-area",
          "ip-reachability-information": "192.168.0.1/32"
        },
        "attributes": {
          "ipv4-next-hop": {
            "global": "172.16.1.85"
          },
          "origin": {
            "value": "igp"
          },
          "prefix-attributes": {
            "prefix-metric": 1
          },
          "as-path": {},
          "local-pref": {
            "pref": 100
          }
        },
        "protocol-id": "ospf"
      }
    ]
  }
}'''

topologyData04={
    "nodes": [
      {
        "deviceType": "Cisco 4451 Series Integrated Services Router",
        "label": "CAMPUS-Router2",
        "ip": "210.2.2.1",
        "softwareVersion": "15.4(3)S",
        "nodeType": "device",
        "family": "Routers",
        "platformId": "ISR4451-X/K9",
        "tags": [],
        "role": "BORDER ROUTER",
        "roleSource": "AUTO",
        "customParam": {},
        "id": "1c1bafb8-529d-41ac-936f-d7366126bbc0"
      },
      {
        "deviceType": "Cisco 3500I Unified Access Point",
        "label": "AP7081.059f.19ca",
        "ip": "55.1.1.3",
        "softwareVersion": "8.1.14.16",
        "nodeType": "device",
        "family": "Unified AP",
        "platformId": "AIR-CAP3502I-A-K9",
        "tags": [],
        "role": "ACCESS",
        "roleSource": "AUTO",
        "customParam": {},
        "id": "29842dd5-f93d-4e8a-8267-b6e791fc0c0d"
      },
      {
        "deviceType": "Cisco 4451 Series Integrated Services Router",
        "label": "CAMPUS-Router1",
        "ip": "210.1.1.1",
        "softwareVersion": "15.4(3)S",
        "nodeType": "device",
        "family": "Routers",
        "platformId": "ISR4451-X/K9",
        "tags": [],
        "role": "BORDER ROUTER",
        "roleSource": "AUTO",
        "customParam": {},
        "id": "2de15337-a9a6-4830-a632-50b2aa65fb9a"
      },
      {
        "deviceType": "Cisco Catalyst 29xx Stack-able Ethernet Switch",
        "label": "Branch-Access1",
        "ip": "207.1.10.1",
        "softwareVersion": "12.2(55)SE3",
        "nodeType": "device",
        "family": "Switches and Hubs",
        "platformId": "WS-C2960S-48LPS-L",
        "tags": [],
        "role": "ACCESS",
        "roleSource": "AUTO",
        "customParam": {},
        "id": "329cfe07-1c38-4f6e-ac59-da5af8a2d9ad"
      },
      {
        "deviceType": "Cisco Catalyst 6503 Switch",
        "label": "CAMPUS-Core2",
        "ip": "211.2.2.1",
        "softwareVersion": "15.1(1)SY3",
        "nodeType": "device",
        "family": "Switches and Hubs",
        "platformId": "WS-C6503-E",
        "tags": [],
        "role": "DISTRIBUTION",
        "roleSource": "AUTO",
        "customParam": {},
        "id": "86f370b0-79cb-40da-adc0-3106c24d03a6"
      },
      {
        "deviceType": "Cisco Catalyst 3850-48U-E Switch",
        "label": "CAMPUS-Access1",
        "ip": "212.1.10.1",
        "softwareVersion": "03.03.00.SE",
        "nodeType": "device",
        "family": "Switches and Hubs",
        "platformId": "WS-C3850-48U",
        "tags": [],
        "role": "ACCESS",
        "roleSource": "AUTO",
        "customParam": {},
        "id": "b488afed-a391-4bf9-8770-eb826d0ee41b"
      },
      {
        "deviceType": "Cisco 2911 Integrated Services Router G2",
        "label": "Branch-Router1",
        "ip": "207.3.1.1",
        "softwareVersion": "15.2(4)M6a",
        "nodeType": "device",
        "family": "Routers",
        "platformId": "CISCO2911/K9",
        "tags": [],
        "role": "BORDER ROUTER",
        "roleSource": "AUTO",
        "customParam": {},
        "id": "b68a5d5c-52e2-4577-8f51-881f396c7b2f"
      },
      {
        "deviceType": "Cisco Catalyst 4507R plus E Switch",
        "label": "CAMPUS-Dist2",
        "ip": "212.3.1.2",
        "softwareVersion": "03.04.00.SG",
        "nodeType": "device",
        "family": "Switches and Hubs",
        "platformId": "WS-C4507R+E",
        "tags": [],
        "role": "DISTRIBUTION",
        "roleSource": "AUTO",
        "customParam": {},
        "id": "c92c9058-3d76-4db3-8020-62ace6dcff76"
      },
      {
        "deviceType": "Cisco 2911 Integrated Services Router G2",
        "label": "Branch-Router2",
        "ip": "207.3.1.2",
        "softwareVersion": "15.2(4)M6a",
        "nodeType": "device",
        "family": "Routers",
        "platformId": "CISCO2911/K9",
        "tags": [],
        "role": "BORDER ROUTER",
        "roleSource": "AUTO",
        "customParam": {},
        "id": "cb05bee0-9900-4ec9-992b-624f0ba6bd19"
      },
      {
        "deviceType": "Cisco 5508 Wireless LAN Controller",
        "label": "Campus-WLC-5508",
        "ip": "55.1.1.2",
        "softwareVersion": "8.1.14.16",
        "nodeType": "device",
        "family": "Wireless Controller",
        "platformId": "AIR-CT5508-K9",
        "tags": [],
        "role": "ACCESS",
        "roleSource": "AUTO",
        "customParam": {},
        "id": "d8381596-6e7b-474b-9ec1-2519915b327a"
      },
      {
        "deviceType": "Cisco Catalyst 6503 Switch",
        "label": "CAMPUS-Core1",
        "ip": "211.1.1.1",
        "softwareVersion": "15.1(1)SY3",
        "nodeType": "device",
        "family": "Switches and Hubs",
        "platformId": "WS-C6503-E",
        "tags": [],
        "role": "DISTRIBUTION",
        "roleSource": "AUTO",
        "customParam": {},
        "id": "db202e09-05a8-4925-9f69-b9f91c1cf6d0"
      },
      {
        "deviceType": "Cisco Catalyst 4507R plus E Switch",
        "label": "CAMPUS-Dist1",
        "ip": "55.1.1.100",
        "softwareVersion": "03.02.00.XO",
        "nodeType": "device",
        "family": "Switches and Hubs",
        "platformId": "WS-C4507R+E",
        "tags": [],
        "role": "DISTRIBUTION",
        "roleSource": "AUTO",
        "customParam": {},
        "id": "e69b8e8b-ab5b-4d13-969e-3fb216ae1367"
      },
      {
        "deviceType": "wireless",
        "label": "65.1.1.46",
        "ip": "65.1.1.46",
        "nodeType": "HOST",
        "family": "WIRELESS",
        "role": "HOST",
        "customParam": {},
        "id": "3bc9818d-7692-43e0-934b-e2fa084c0c7f"
      },
      {
        "deviceType": "wired",
        "label": "207.1.10.20",
        "ip": "207.1.10.20",
        "nodeType": "HOST",
        "family": "WIRED",
        "role": "HOST",
        "customParam": {},
        "id": "4c7f676f-2c89-4fcf-af1a-a06839a74e3b"
      },
      {
        "deviceType": "wired",
        "label": "212.1.10.20",
        "ip": "212.1.10.20",
        "nodeType": "HOST",
        "family": "WIRED",
        "role": "HOST",
        "customParam": {},
        "id": "69cdd203-044f-467b-a922-3470e0edcd69"
      },
      {
        "deviceType": "cloud node",
        "label": "cloud node",
        "ip": "UNKNOWN",
        "softwareVersion": "UNKNOWN",
        "nodeType": "cloud node",
        "family": "cloud node",
        "platformId": "UNKNOWN",
        "tags": [
          "cloud node"
        ],
        "role": "cloud node",
        "roleSource": "AUTO",
        "customParam": {
          "x": 9,
          "y": -4
        },
        "id": "dfa3d2e0-99da-4f42-a822-c9dbccb0d56b"
      }
    ],
    "links": [
      {
        "source": "db202e09-05a8-4925-9f69-b9f91c1cf6d0",
        "startPortID": "399a91bb-7a4e-45ca-b6af-b0756e94ef2a",
        "startPortName": "TenGigabitEthernet1/4",
        "startPortIpv4Address": "211.3.1.1",
        "startPortIpv4Mask": "255.255.255.252",
        "startPortSpeed": "10000000",
        "target": "86f370b0-79cb-40da-adc0-3106c24d03a6",
        "endPortID": "3c46ab62-c205-4f83-a0cd-64c5dfc5c35e",
        "endPortName": "TenGigabitEthernet1/4",
        "endPortIpv4Address": "211.3.1.2",
        "endPortIpv4Mask": "255.255.255.252",
        "endPortSpeed": "10000000",
        "linkStatus": "up",
        "id": "93101"
      },
      {
        "source": "b488afed-a391-4bf9-8770-eb826d0ee41b",
        "startPortID": "c803a115-927f-455d-8fba-3dc6b90cb7c7",
        "startPortName": "GigabitEthernet1/0/2",
        "startPortSpeed": "1000000",
        "target": "c92c9058-3d76-4db3-8020-62ace6dcff76",
        "endPortID": "baf4a3c2-87e8-4369-aa07-1deabf89dbb4",
        "endPortName": "GigabitEthernet5/5",
        "endPortSpeed": "1000000",
        "linkStatus": "up",
        "id": "93108"
      },
      {
        "source": "db202e09-05a8-4925-9f69-b9f91c1cf6d0",
        "startPortID": "b3dacdf1-7c5c-42a3-8581-5de1522e6c65",
        "startPortName": "GigabitEthernet1/1",
        "startPortIpv4Address": "211.1.1.1",
        "startPortIpv4Mask": "255.255.255.252",
        "startPortSpeed": "1000000",
        "target": "e69b8e8b-ab5b-4d13-969e-3fb216ae1367",
        "endPortID": "058a7b37-49fe-46ce-a3be-182874058cb8",
        "endPortName": "GigabitEthernet5/7",
        "endPortIpv4Address": "211.1.1.2",
        "endPortIpv4Mask": "255.255.255.252",
        "endPortSpeed": "1000000",
        "linkStatus": "up",
        "id": "93099"
      },
      {
        "source": "329cfe07-1c38-4f6e-ac59-da5af8a2d9ad",
        "startPortID": "e6b575db-fbfe-4c5b-89b3-700ae1d3a8af",
        "startPortName": "GigabitEthernet1/0/2",
        "startPortSpeed": "1000000",
        "target": "b68a5d5c-52e2-4577-8f51-881f396c7b2f",
        "endPortID": "7d5f86e9-e681-44b7-9573-0c44ce040d10",
        "endPortName": "GigabitEthernet0/2",
        "endPortIpv4Address": "207.1.10.2",
        "endPortIpv4Mask": "255.255.255.0",
        "endPortSpeed": "1000000",
        "linkStatus": "up",
        "id": "93094"
      },
      {
        "source": "db202e09-05a8-4925-9f69-b9f91c1cf6d0",
        "startPortID": "5006f8b2-ab37-423d-ba20-8671ae66e4f8",
        "startPortName": "GigabitEthernet1/3",
        "startPortIpv4Address": "210.2.2.2",
        "startPortIpv4Mask": "255.255.255.252",
        "startPortSpeed": "1000000",
        "target": "1c1bafb8-529d-41ac-936f-d7366126bbc0",
        "endPortID": "f841fd3e-cf36-4722-9b52-6c04e4d0055a",
        "endPortName": "GigabitEthernet0/0/0",
        "endPortIpv4Address": "210.2.2.1",
        "endPortIpv4Mask": "255.255.255.252",
        "endPortSpeed": "1000000",
        "linkStatus": "up",
        "id": "93103"
      },
      {
        "source": "b68a5d5c-52e2-4577-8f51-881f396c7b2f",
        "startPortID": "5d5b37b6-1443-4e70-8353-410378e1e33c",
        "startPortName": "GigabitEthernet0/1",
        "startPortIpv4Address": "207.3.1.1",
        "startPortIpv4Mask": "255.255.255.0",
        "startPortSpeed": "1000000",
        "target": "cb05bee0-9900-4ec9-992b-624f0ba6bd19",
        "endPortID": "a07b8ff7-6c3d-4ed9-922e-e59123591830",
        "endPortName": "GigabitEthernet0/1",
        "endPortIpv4Address": "207.3.1.2",
        "endPortIpv4Mask": "255.255.255.0",
        "endPortSpeed": "1000000",
        "linkStatus": "up",
        "id": "93093"
      },
      {
        "source": "2de15337-a9a6-4830-a632-50b2aa65fb9a",
        "startPortID": "8888dd78-1962-4942-a04e-dccc2c9fcd59",
        "startPortName": "GigabitEthernet0/0/2",
        "startPortIpv4Address": "210.3.1.1",
        "startPortIpv4Mask": "255.255.255.252",
        "startPortSpeed": "1000000",
        "target": "1c1bafb8-529d-41ac-936f-d7366126bbc0",
        "endPortID": "e1b2e9b7-f27b-489a-85f4-2f4016289677",
        "endPortName": "GigabitEthernet0/0/2",
        "endPortIpv4Address": "210.3.1.2",
        "endPortIpv4Mask": "255.255.255.252",
        "endPortSpeed": "1000000",
        "linkStatus": "up",
        "id": "93109"
      },
      {
        "source": "29842dd5-f93d-4e8a-8267-b6e791fc0c0d",
        "startPortID": "",
        "startPortName": "GigabitEthernet0",
        "startPortIpv4Address": " 55.  1.  1.  3",
        "startPortIpv4Mask": "255.255.255.  0",
        "startPortSpeed": "-1",
        "target": "b488afed-a391-4bf9-8770-eb826d0ee41b",
        "endPortID": "6f266ea3-286a-47f9-992f-c4a2782bc8b4",
        "endPortName": "GigabitEthernet1/0/26",
        "endPortSpeed": "1000000",
        "linkStatus": "up",
        "id": "93110"
      },
      {
        "source": "b488afed-a391-4bf9-8770-eb826d0ee41b",
        "startPortID": "6e63592c-a536-4866-9db2-fe87255e64f8",
        "startPortName": "GigabitEthernet1/0/1",
        "startPortSpeed": "1000000",
        "target": "e69b8e8b-ab5b-4d13-969e-3fb216ae1367",
        "endPortID": "bc380128-b072-4ab7-a561-2864d8fe5c39",
        "endPortName": "GigabitEthernet5/5",
        "endPortSpeed": "1000000",
        "linkStatus": "up",
        "id": "93097"
      },
      {
        "source": "86f370b0-79cb-40da-adc0-3106c24d03a6",
        "startPortID": "b30f523b-ae44-4067-96a4-f396302ffe6b",
        "startPortName": "GigabitEthernet1/3",
        "startPortIpv4Address": "210.2.1.2",
        "startPortIpv4Mask": "255.255.255.252",
        "startPortSpeed": "1000000",
        "target": "1c1bafb8-529d-41ac-936f-d7366126bbc0",
        "endPortID": "d67b89bd-11bb-4b6b-ab52-f3790c8b67b8",
        "endPortName": "GigabitEthernet0/0/1",
        "endPortIpv4Address": "210.2.1.1",
        "endPortIpv4Mask": "255.255.255.252",
        "endPortSpeed": "1000000",
        "linkStatus": "up",
        "id": "93104"
      },
      {
        "source": "e69b8e8b-ab5b-4d13-969e-3fb216ae1367",
        "startPortID": "d56c2409-0fa3-4b03-900d-b00a2133be01",
        "startPortName": "GigabitEthernet5/48",
        "startPortIpv4Address": "212.3.1.1",
        "startPortIpv4Mask": "255.255.255.252",
        "startPortSpeed": "1000000",
        "target": "c92c9058-3d76-4db3-8020-62ace6dcff76",
        "endPortID": "a368d302-58bb-4245-bc76-82b83b94eb53",
        "endPortName": "GigabitEthernet5/48",
        "endPortIpv4Address": "212.3.1.2",
        "endPortIpv4Mask": "255.255.255.252",
        "endPortSpeed": "1000000",
        "linkStatus": "up",
        "id": "93098"
      },
      {
        "source": "86f370b0-79cb-40da-adc0-3106c24d03a6",
        "startPortID": "83cfeccb-ed87-49ce-bc91-4c93eb60c719",
        "startPortName": "TenGigabitEthernet1/5",
        "startPortIpv4Address": "211.2.2.1",
        "startPortIpv4Mask": "255.255.255.252",
        "startPortSpeed": "10000000",
        "target": "e69b8e8b-ab5b-4d13-969e-3fb216ae1367",
        "endPortID": "5df615f9-d36b-49df-9ae7-708e153d1765",
        "endPortName": "TenGigabitEthernet3/1",
        "endPortIpv4Address": "211.2.2.2",
        "endPortIpv4Mask": "255.255.255.252",
        "endPortSpeed": "10000000",
        "linkStatus": "up",
        "id": "93100"
      },
      {
        "source": "329cfe07-1c38-4f6e-ac59-da5af8a2d9ad",
        "startPortID": "379ddcf8-23f2-423f-af24-526ed3ba275d",
        "startPortName": "GigabitEthernet1/0/1",
        "startPortSpeed": "1000000",
        "target": "cb05bee0-9900-4ec9-992b-624f0ba6bd19",
        "endPortID": "6257d59c-4bec-4268-94c2-a85163d74478",
        "endPortName": "GigabitEthernet0/2",
        "endPortIpv4Address": "207.1.10.3",
        "endPortIpv4Mask": "255.255.255.0",
        "endPortSpeed": "1000000",
        "linkStatus": "up",
        "id": "93095"
      },
      {
        "source": "86f370b0-79cb-40da-adc0-3106c24d03a6",
        "startPortID": "ea0cb498-cabf-404d-a57a-676e6e38077e",
        "startPortName": "GigabitEthernet1/2",
        "startPortIpv4Address": "210.1.2.2",
        "startPortIpv4Mask": "255.255.255.252",
        "startPortSpeed": "1000000",
        "target": "2de15337-a9a6-4830-a632-50b2aa65fb9a",
        "endPortID": "40fc3c1f-833d-479f-b8c1-722ee6f0c9e5",
        "endPortName": "GigabitEthernet0/0/1",
        "endPortIpv4Address": "210.1.2.1",
        "endPortIpv4Mask": "255.255.255.252",
        "endPortSpeed": "1000000",
        "linkStatus": "up",
        "id": "93106"
      },
      {
        "source": "86f370b0-79cb-40da-adc0-3106c24d03a6",
        "startPortID": "b825f311-c776-4181-9c73-e0609639fc4d",
        "startPortName": "GigabitEthernet1/1",
        "startPortIpv4Address": "211.2.1.1",
        "startPortIpv4Mask": "255.255.255.252",
        "startPortSpeed": "1000000",
        "target": "c92c9058-3d76-4db3-8020-62ace6dcff76",
        "endPortID": "87b7094d-ea25-48ac-9f9a-7bec9ab09e95",
        "endPortName": "GigabitEthernet5/7",
        "endPortIpv4Address": "211.2.1.2",
        "endPortIpv4Mask": "255.255.255.252",
        "endPortSpeed": "1000000",
        "linkStatus": "up",
        "id": "93107"
      },
      {
        "source": "db202e09-05a8-4925-9f69-b9f91c1cf6d0",
        "startPortID": "96fed199-c14b-4222-8d97-89f79cbb6084",
        "startPortName": "TenGigabitEthernet1/5",
        "startPortIpv4Address": "211.1.2.1",
        "startPortIpv4Mask": "255.255.255.252",
        "startPortSpeed": "10000000",
        "target": "c92c9058-3d76-4db3-8020-62ace6dcff76",
        "endPortID": "2a44f00a-7d2b-4202-be3b-ca10ce735db9",
        "endPortName": "TenGigabitEthernet3/1",
        "endPortIpv4Address": "211.1.2.2",
        "endPortIpv4Mask": "255.255.255.252",
        "endPortSpeed": "10000000",
        "linkStatus": "up",
        "id": "93102"
      },
      {
        "source": "e69b8e8b-ab5b-4d13-969e-3fb216ae1367",
        "startPortID": "bf51a78e-c2ed-4064-8466-f905b8bd7e3f",
        "startPortName": "GigabitEthernet5/38",
        "startPortSpeed": "1000000",
        "target": "d8381596-6e7b-474b-9ec1-2519915b327a",
        "endPortID": "12b72d31-1042-4f8d-82f0-0f3ad97c79e3",
        "endPortName": "GigabitEthernet0/0/1",
        "endPortSpeed": "1000000",
        "linkStatus": "up",
        "id": "93096"
      },
      {
        "source": "db202e09-05a8-4925-9f69-b9f91c1cf6d0",
        "startPortID": "2eafa7e2-8c5a-480b-afe3-5d8fd6d01769",
        "startPortName": "GigabitEthernet1/2",
        "startPortIpv4Address": "210.1.1.2",
        "startPortIpv4Mask": "255.255.255.252",
        "startPortSpeed": "1000000",
        "target": "2de15337-a9a6-4830-a632-50b2aa65fb9a",
        "endPortID": "279429fe-8a9f-485d-a2be-c7e15aaa2610",
        "endPortName": "GigabitEthernet0/0/0",
        "endPortIpv4Address": "210.1.1.1",
        "endPortIpv4Mask": "255.255.255.252",
        "endPortSpeed": "1000000",
        "linkStatus": "up",
        "id": "93105"
      },
      {
        "source": "29842dd5-f93d-4e8a-8267-b6e791fc0c0d",
        "target": "3bc9818d-7692-43e0-934b-e2fa084c0c7f",
        "linkStatus": "UP"
      },
      {
        "source": "329cfe07-1c38-4f6e-ac59-da5af8a2d9ad",
        "startPortID": "5122fd16-074c-429a-8de2-61922b059dd7",
        "target": "4c7f676f-2c89-4fcf-af1a-a06839a74e3b",
        "linkStatus": "UP"
      },
      {
        "source": "b488afed-a391-4bf9-8770-eb826d0ee41b",
        "startPortID": "7f34679a-3113-40d5-846c-f5a4a30d8bbf",
        "target": "69cdd203-044f-467b-a922-3470e0edcd69",
        "linkStatus": "UP"
      },
      {
        "source": "dfa3d2e0-99da-4f42-a822-c9dbccb0d56b",
        "target": "1c1bafb8-529d-41ac-936f-d7366126bbc0",
        "linkStatus": "up"
      },
      {
        "source": "dfa3d2e0-99da-4f42-a822-c9dbccb0d56b",
        "target": "2de15337-a9a6-4830-a632-50b2aa65fb9a",
        "linkStatus": "up"
      },
      {
        "source": "dfa3d2e0-99da-4f42-a822-c9dbccb0d56b",
        "target": "b68a5d5c-52e2-4577-8f51-881f396c7b2f",
        "linkStatus": "up"
      },
      {
        "source": "dfa3d2e0-99da-4f42-a822-c9dbccb0d56b",
        "target": "cb05bee0-9900-4ec9-992b-624f0ba6bd19",
        "linkStatus": "up"
      }
    ]
};
topology={}
node={}
node_list=[]
link={}
links=[]
node_count=0
node_x=0
node_y=0
Topo_URL_data='http://127.0.0.1:7778/data'

url = "http://10.75.195.243:8181/restconf/operational/bgp-rib:bgp-rib/rib/bgp-example/loc-rib/tables/bgp-linkstate:linkstate-address-family/bgp-linkstate:linkstate-subsequent-address-family/linkstate-routes"
credentials = base64.b64encode(b'admin:admin')
payload = "<neighbor xmlns=\"urn:opendaylight:params:xml:ns:yang:bgp:openconfig-extensions\">\n    <neighbor-address>172.16.1.85</neighbor-address>\n    <afi-safis>\n        <afi-safi>\n            <afi-safi-name>LINKSTATE</afi-safi-name>\n        </afi-safi>\n    </afi-safis>\n</neighbor>"
headers = {
    'content-type': "application/xml",
    'authorization': "Basic "+credentials,
    'cache-control': "no-cache",
    'postman-token': "b9fc303a-eab9-3a73-66e0-14e86e06f580"
    }

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    
    node={}
    node_list=[]
    link={}
    links=[]
    node_count=0
    node_x=0
    node_y=0


    response = requests.request("GET", url, data=payload, headers=headers)

    print(response.text)
    Result=response.text

    print type(topologyData01)

    Node_dict={}

    node_count=0
    node_x_low=100
    node_x_up=300
    node_y_low=100
    node_y_up=300
    
    Resault_json=json.loads(Result)
#print type(Resault_json)    #type dict
    Result_Link_state_Routes=Resault_json["bgp-linkstate:linkstate-routes"]["linkstate-route"]

#print type(Result_Link_state_Routes)   #type list
    
    for i in Result_Link_state_Routes:
        if "prefix-descriptors" in i:
            print "PREFIX information"
            print "OSPF ID"+str(i["advertising-node-descriptors"]["ospf-node"]["ospf-router-id"])
            print "Prefix "+i["prefix-descriptors"]["ip-reachability-information"]
    
        if "node-descriptors" in i:
            print "NODE information"
            print "OSPF ID"+str(i["node-descriptors"]["ospf-node"]["ospf-router-id"])
            print "IP address"+i["attributes"]["node-attributes"]["ipv4-router-id"]
            node_count=node_count+1
            node_x=random.randint(node_x_low,node_x_up)           
            node_y=random.randint(node_y_low,node_y_up)
            Node_dict[i["attributes"]["node-attributes"]["ipv4-router-id"]]=str(node_count)
            node["id"]=node_count
            node["name"]=i["attributes"]["node-attributes"]["ipv4-router-id"]
            node["x"]=node_x
            node["y"]=node_y
            copy_node=copy.deepcopy(node)
            print node_x
            print node_y
            node_list.append(copy_node)
            print "-----------------------------------------------------------"

    for i in Result_Link_state_Routes:
        if "link-descriptors" in i:
            print "LINK information"
            print "Link from node "+i["attributes"]["link-attributes"]["local-ipv4-router-id"]+\
              " local ip address "+i["link-descriptors"]["ipv4-interface-address"]+\
              "  to Remote node "+i["attributes"]["link-attributes"]["remote-ipv4-router-id"]+\
              " remote ip address  "+i["link-descriptors"]["ipv4-neighbor-address"]
            print "Local Node id "+Node_dict[i["attributes"]["link-attributes"]["local-ipv4-router-id"]]+"  to  Remote node id "+\
                Node_dict[i["attributes"]["link-attributes"]["remote-ipv4-router-id"]]
            link["source"]=Node_dict[i["attributes"]["link-attributes"]["local-ipv4-router-id"]]
            link["target"]=Node_dict[i["attributes"]["link-attributes"]["remote-ipv4-router-id"]]
            copy_link=copy.deepcopy(link)
            links.append(copy_link)
              
              

    print node_list
    print links

    topology["nodes"]=node_list
    topology["links"]=links#return '<h1>Home</h1>'
    text='''Home index page '''
    print text
    return render_template('index.html',text="home")

@app.route('/data', methods=['GET', 'POST'])
def data():
    #return '<h1>Home</h1>'
    text='''REST API provides JASON topology data '''
    print text
    node_name="Alex1111"
    return  jsonify(topology)

@app.route('/top1',methods=['GET','POST'])
def top1():
    text='topology1'
    print "display topology1"
    return render_template('index.html',text="http://127.0.0.1:7778/data")

if __name__ == '__main__':
    

    app.run(host="127.0.0.1", port=int("7778"))