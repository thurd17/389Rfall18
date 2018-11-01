#!/usr/bin/env python2

import sys
import struct
import random
from datetime import datetime


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


f = open("details.txt","w")

def process_words(text,length):
    i = 0
    result = []
    for c in text[4:4+length]:
        if i % 4 == 0:
            result.append(ord(c))
            i = i + 1 
        else:
            i = i + 1
    f.write(str(result))
    return length

def process_ascii(text,length):
    f.write(text[4:4+length])
    return length

def process_coord(text,length):
    x,y = struct.unpack("<dd", text[4:4+length]) 
    f.write("(" + str(x) + ", " + str(y) + ")")

def process_ref(text,length):
    length,val = struct.unpack("<LL",text[0:4+length])
    f.write( "Reference to section %s" % val)

def process_png(text,length):
    filename = "extractedPNG" + str(random.randint(1,20)) + ".png"
    f.write(filename)
    with open(filename,"wb") as output:
        output.write(chr(0x89))
        output.write(chr(0x50))
        output.write(chr(0x4e))
        output.write(chr(0x47))
        output.write(chr(0x0d))
        output.write(chr(0x0a))
        output.write(chr(0x1a))
        output.write(chr(0x0a))
        output.write(text[4:4+length])
    return length
    

def process_dword(text,length):
    i = 0
    result = []
    for c in text[4:4+length]:
        if i % 8 == 0:
            result.append(ord(c))
            i = i + 1
        else:
            i = i + 1
    f.write(str(result))

# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()


# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8]) 
version, timestamp  = struct.unpack("<LL",data[4:12])
section_num, type_section = struct.unpack("<LL", data[20:28])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))


f.write("------- HEADER -------\n")
f.write("MAGIC: %s\n" % hex(magic))
f.write("VERSION: %d\n" % int(version))
f.write("TIMESTAMP: ")
f.write(datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S'))
f.write("\nAUTHOR: %s\n" % data[12:20])
f.write("SECTION NUMBER: %s\n" % section_num)



# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!
f.write( "-------  BODY  -------\n") 
offset = 24
count = 1
while(count != 12):
    type_section,length = struct.unpack("<LL",data[offset:offset+8])
    f.write("\n")
    if (type_section == 9):
        f.write("Section: %s Type: ASCII\n" % count)
        result = process_ascii(data[offset+4:],length)
        offset = offset + length + 8
        count = count + 1
        f.write("\n")
    elif (type_section == 7):
        f.write( "Section: %s Type: Reference\n" % count)
        result = process_ref(data[offset+4:],length)
        count = count + 1
        offset = offset + length + 8
        f.write("\n")
    elif (type_section == 6):
        f.write("Section: %s Type: Coordinate\n" % count)
        result = process_coord(data[offset+4:],length)
        count = count + 1
        offset = offset + length + 8
        f.write("\n")
    elif (type_section == 5):
        f.write("Section: %s Type: Array of Words\n" % count)
        result = process_words(data[offset+4:],length)
        offset = offset + length + 8
        count = count + 1
        f.write("\n")
    elif (type_section == 4):
        f.write("Section: %s Type: Array of Doubles\n" % count)
        offset = offset + length + 8
        count = count + 1
        f.write("\n")
    elif (type_section == 3):
        f.write( "Section: %s Type: UTF text\n" % count)
        count = count + 1
        f.write("\n")
    elif (type_section == 2):
        f.write("Section: %s Type: Array of DWORDS\n" % count)
        result = process_dword(data[offset+4:],length)
        offset = offset + length + 8
        count = count + 1
        f.write("\n")
    elif (type_section == 1):
        f.write("Section: %s Type: PNG\n" % count)
        result = process_png(data[offset+4:],length)
        count = count + 1
        offset = offset + length + 8
        f.write("\n")
print "File parsed successfully. Data wrote to details.txt.\n"
