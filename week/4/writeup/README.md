Writeup 3 - Pentesting I
======

Name: Tumie Hurd
Section: 0101

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Tumie Hurd

## Assignment 4 Writeup

### Part 1 (45 pts)

For the new Cornerstone Airlines uptime system, I began looking for vulnerabilities.  I ran the command
```nc cornerstoneairlines.co 45``` which led me to a prompt for an IP address.

Next, I entered umd.edu as a test website and it returned information about the connection to that website. I began trying to add commands to the end of the domain name (ex ```umd.edu; ls``` ). I kept experimenting with different commands and eventually realized that I could simply use a semicolon and did not even need to input an IP address. I used ```ls``` and began going through files in the directory.  I first searched in ```/home``` because this was where the user's personal files are usually located.  This is where I found the flag.txt file.

In the prompt for the IP address, I entered ```; cat home/flag.txt``` which returned the flag ```CMSC389R-{p1ng_as_a_$erv1c3}```.


Next, I began looking for the script that Fred uses to check the uptime. I didn't feel like looking through all off the directories, so I looked online and found the "find" command.

I ran the following command which showed me four different scripts.
```; && find . -name *.sh```

The scripts that were located were
* ./opt/container_startup.sh
* ./usr/share/debconf/confmodule.sh
* ./lib/init/vars.sh
* ./etc/init.d/hwclock.sh

After looking through these scripts, it seemed as if ```./opt/container_startup.sh``` was the file that I was looking for.  When I first opened the file, I had a bit of trouble understanding what the script was doing, but after researching online I was able to get some understanding.  The script appends the input from the user to the end of a string with a ping command.  This string is stored in the variable ```cmd```.  This string is then executed by the eval command and the output is stored in the variable ```output``` which is then echoed to the user.


How Fred can protect his system from this vulnerability.

Fred can better secure his system if he sanitizes his inputs.  In Fred's script, whatever additional text that the user provides is added to the end of the ping command.  He could do some sort of pattern matching for an IP address or a domain name.  He could also not allow spaces and characters such as "&&" and ";" which make it easy for command injection attacks to occur. 

### Part 2 (55 pts)

For the second part of this assignment, I was tasked with writing code for a shell that would leverage this vulnerability. I chose to write the program in python using the skeleton code that was provided.  I first started by making sure I could connect to the server and ping a specific IP.  Next, I tested sending some commands at the end of the IP.  I used the split() function to parse the response from the server so it would only display the information that was related to the command.  Doing simple commands such as ```ls``` and ```cat``` worked fine but I was having trouble with the ```cd``` command.  With more time, I could have implemented a better parser to work with the cd command but currently it is very minimal. For the ```cd``` command, I had to reconnct to the server after ever command so it did not preserve the state.  I tried storing the current directory in a variable, but I was having trouble adding and deleting directories from the variable when going up and down levels.  The ```quit``` and ```exit``` commands were easy to implement. The ```pull``` command took some effort because I had to read in all of the information from the source file into a variable and then write it to the destination location. My pull command only works if the file is under 4000 bytes.  I know that there is a "correct" way to process the pull command but this was the easiest way that I knew.