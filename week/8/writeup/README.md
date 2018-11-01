Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: Tumie Hurd
Section: 0101

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Tumie Hurd

## Assignment 8 Writeup

### Part 1 (45 Pts)
1. The hackers used the traceroute command on csec-vip.umiacs.umd.edu.
This was found by finding the IP in the pcap and then doing a reverse DNS lookup by running ```host 128.8.120.53```.


2. The names used by the hackers are "c0uchpot4doz" and "laz0rh4x".

3. c0uchpot4doz ip address is 142.93.118.186 and laz0rh4x ip address is 104.248.224.85. 

4. They are using ports 2749.

5. They mentioned plans and sent a file that could be read with the parser that laz0rh4x had previously provided. heir plans are taking place "tomorrow at 1500".

6. laz0rh4x sent the file, update.fpff, by way of a google drive link https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing 

7.They plan to see each other again "tomorrow at 1500".

### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*
1. upate.fpff was generated at ```2018-10-25 00:40:07```.

2. The file was authored by ```laz0rh4x```.

3. The file states that it has 9 sections but actually has 11.

4. ```------- HEADER -------
MAGIC: 0xdeadbeef
VERSION: 1
TIMESTAMP: 2018-10-25 00:40:07
AUTHOR: laz0rh4x
SECTION NUMBER: 9
-------  BODY  -------

Section: 1 Type: ASCII
Call this number to get your flag: (422) 537 - 7946

Section: 2 Type: Array of Words
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]

Section: 3 Type: Coordinates
(38.99161, -77.02754)

Section: 4 Type: Reference
Reference to section 1

Section: 5 Type: ASCII
The imfamous security pr0s at CMSC389R will never find this!

Section: 6 Type: ASCII
The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.[4}

Section: 7 Type: Coordinate
(38.9910941, -76.9328019)

Section: 8 Type: PNG
extractedPNG1.png

Section: 9 Type: ASCII
AF(saSAdf1AD)Snz**asd1

Section: 10 Type: ASCII
Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9

Section: 11 Type: Array of DWORDS
[4, 8, 15, 16, 23, 42]```

5. ```CMSC389R-{c0rn3rst0ne_airlin3s_to_the_moon}``` was found inside of the extracted png.
```CMSC389R-{h1dd3n-s3ct10n-1n-f1l3}``` was found by using the base 64 decoding of the text found in section 10.
I called the number from section 1, but there was no flag associated with it.
