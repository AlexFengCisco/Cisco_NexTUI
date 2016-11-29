## Cisco NexT UI for network topolopy
####prepare the lab

     download NeXt UI zip file via [Cisco DevNet ](https://developer.cisco.com/fileMedia/download/025dc509-8f2a-474a-b6d8-75e73ecbd6ac).
     copy unzipped files to work space folder 
     create nextapp.py
     
     or, git clone this repo 
#### start with python nextapp.py and web service will listen on port 7778

    from web browser http://127.0.0.1:7778
    topology will be shown in page
    
    modify nextapp.py topologydata object will change the topology
    
    @/data returns jsonity(topologydat)
    javascript ajax call http://127.0.0.1:7778/data to get remote topology data and draw a network topology
    
#### developer may focus on background python to deal with logical issue
