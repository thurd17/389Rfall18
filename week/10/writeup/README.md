Writeup 10 - Crypto II
=====

Name: Tumie Hurd  
Section: 0101  

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.  

Digital acknowledgement of honor pledge: Tumie Hurd  

## Assignment 10 Writeup  

### Part 1 (70 Pts)  
The program works by signing a legit message and receiving a hash. The hash object is then initialized with the state of a vulnerable hash.  We do not know the value of the secret, but because we know that it is between 6 and 15 bytes long, we have to try all ten possible options. Next, the payload is crafted.  They payload consists of the original message plus the padding and the malicious text.  The values for the padding will change at every iteration since the size of the secret will be increasing by 8 bits. Eventually the program will find data that it has not signed before and reveal the flag.       

The flag that was found was ```CMSC389R-{i_still_put_the_M_between_the_DV}```.  
  

### Part 2 (30 Pts)  

To generate my own public and private key pair, I ran the following command.  
```gpg --gen-key```  

To add the UMD Cyber Security public key, I used the following command.  
```gpg --import pgpasignment.key```  

To encrypt the file I named message.txt, I ran the following command.  
```gpg -e -u "Tumie" -r "UMD Cybersecurity Club" message.txt```  



