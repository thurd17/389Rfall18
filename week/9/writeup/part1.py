#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("../probable-v2-top1575.txt", 'r').read().split("\n")

# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

hashes = open("hashes","r").read().split("\n")

def find_password(hsh):
    for word in wordlist:
        for c in salts:
            m = hashlib.sha512(c + word).hexdigest()
            if (m == hsh):
                print "SHA512 hash: " + hsh
                print "Salt: " + c 
                print "Password: " + word,
                break
        
for h in hashes:
    if h != "":
        find_password(h)
        print "\n"

