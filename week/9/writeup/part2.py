#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib

host = "142.93.117.193"   # IP address or URL
port = 7331     # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# receive some data
data = s.recv(1024)
print data
hash_type = data.split(" ")[9]
val = data.split()[15]

while True:
    
    hash_str = "hashlib." + hash_type +"(\"" + val + "\").hexdigest()"
    hsh = eval(hash_str)
    print hsh
    s.send(hsh + "\n")
    data = s.recv(1024)
    print data

    if len(data.split()) > 8:
        hash_type =  data.split()[4]
        val = data.split()[7]
    else :
        break

# close the connection
s.close()
