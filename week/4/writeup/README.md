Writeup 3 - Pentesting I
======

Name: Tumie Hurd
Section: 0101

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Tumie Hurd

## Assignment 4 Writeup

### Part 1 (45 pts)

For the new Cornerstone Airlines uptime system, I began looking for vulnerabilities.
I ran the command ```nc cornerstoneairlines.co 45``` which led me to a prompt for an IP address.

Next, I entered a random website an it returned information about the connection to that website. I began trying to add commands to the end of the websites. I used ls and began going through files in the directory.  I first searched in /home because this was where the user's personal files are usually located.  This is where I found theflag.txt.

In the prompt for the IP address, I entered ```umd.edu && cat home/flag.txt``` which returned the flag ```CMSC389R-{p1ng_as_a_$erv1c3}```.


Next, I began looking for the script that fred uses to check the uptime. I didn't feel like looking through all off the directories so I looked online and found the "find" command.

I ran the following command which showed me four different scripts.

```umd.edu && find . -name *.sh```

The scripts that were located were
* ./opt/container_startup.sh
* ./usr/share/debconf/confmodule.sh
* ./lib/init/vars.sh
* ./etc/init.d/hwclock.sh

After looking through these scripts, it seemed as if ```./opt/container_startup.sh``` was the file that I was looking for.  When I first opened the file, I had a bit of trouble understanding what the script was doing, but after researching online I was able to get some understanding.


How Fred can protect his system from this vulnerability.


### Part 2 (55 pts)
*Put your writeup >= 200 words here in response to part 2 prompt. Your code for part 2 should be copied into a file in the /writeup directory and pushed there as well*
