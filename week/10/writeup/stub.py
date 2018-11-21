#!/usr/bin/env python2
# from the git repo
import md5py
import socket
import struct
import time
#####################################
### STEP 1: Calculate forged hash ###
#####################################
host = "142.93.118.186"
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

data = s.recv(1024)
print data
s.send("1\n")

data = s.recv(1024)
print data

message = 'CMSC389R_Rocks'    # original message here
s.send(message + "\n")
data = s.recv(1024)
print data
legit = data.split()[7]      # a legit hash of secret + message goes here, obtained from signing a message


# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

malicious = 'maliciousTXT'  # put your malicious message here

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()
#print(fake_hash)


#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits
# 48 + 56 + 408



i = 6 
while (i < 16):
    padding = '\x80'

    offset = 64-1-8-len(message)-i

    j = 0
    while j < offset:
        padding += '\x00'
        j= j+1
    
    padding += struct.pack('<B',8*(len(message) + i))
    padding += '\x00\x00\x00\x00\x00\x00\x00'

# payload is the message that corresponds to the hash in `fake_hash`
# server will calculate md5(secret + payload)
#                     = md5(secret + message + padding + malicious)
#                     = fake_hash
    payload = message + padding + malicious

# send `fake_hash` and `payload` to server (manually or with sockets)
# REMEMBER: every time you sign new data, you will regenerate a new secret!
    print payload
    print data ,
    print "2"
    s.send("2\n")
    data = s.recv(1024)
    print data , 
    print fake_hash

    s.send(fake_hash + "\n")
    data = s.recv(1024)
    print data , 
    print payload

    s.send(payload + "\n")
    time.sleep(2)
    data = s.recv(1024)
    print data
    i= i+1    
s.close
