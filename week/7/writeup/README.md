Writeup 7 - Forensics I
======

Name: Tumie Hurd
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Tumie Hurd

## Assignment 7 writeup

### Part 1 (40 pts)

1. What kind of file is it? JPEG

2. Where was the photo taken? The photo was taken at the GPS position ```41 deg 53' 54.87" N, 87 deg 37' 22.53" W``` which is In Chicago at the John Hancock Center.

3. When was this photo taken? 2018:08:22 11:33:24

4. What kind of camera took this photo? iPhone 8

5. How high up was the photo taken? 539.5m above sea level

6. Found flags:  
I ran ```strings image | grep "CMSC"``` to find the flag ```CMSC389R-{look_I_f0und_a_str1ng}```.

I used ```binwalk --dd='.*' image``` to extract the files within the image and find the flag ```CMSCR-{abr@cadabra}``` inside the png file.  

### Part 2 (55 pts)

I tried using the strings command to locate any text within the binary that matched with CMSC but I could not find any matches.  I then tried using objdump to view the assembly instructions but there were far too many instructions to pull any meaningful data from.  I then used gdb and ran ```disassemble main``` to give me a more consice view.  I saw that a number of hex values were being moved and after converting these values to ascii discoved that it was ```/tmp/.stego```.  I was trying to figure out how to open the file so I copied it to my current directory and then ran ```file stego``` which returned that it was data.  Next, I ran ```xxd stego | head``` to see the magic bytes of the file.  I then used hexedit to attempt to change the bytes so it would match that of a JPEG but it wouldn't allow me to delete bytes so I had to run the command ```tail -c +2 stego > newFile```.  This allowed me to be able to open the JPEG file.  Next, I tried to use steghide to extract the file but it was password protcted.  I found a shell script online that would perform brute force attacks on password protected files.  I ran this script with rockyou.txt and found the password ```stegosaurus```.  The flag found was ```CMSC389R-{dropping_files_is_fun}``` .  