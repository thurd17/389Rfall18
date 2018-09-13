Writeup 2 - OSINT (Open Source Intelligence)
======

Name: Tumie Hurd
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Tumie Hurd

## Assignment 2 writeup

### Part 1 (45 pts)

1. What is Kruegster1990's real name?
Fred Krueger

2. List all personal information (including social media accounts) you can find abut him.
Email: kruegster@tutanota.com
Twitter.com/kruegster1990
Instagram.com/kruegster1990
Reddit.com/user/kruegster1990

3. What is the IP address of the webserver hosting his company's site?
The IP address is 142.93.118.186 and I discovered this by pinging the domain name.

4. List any hidden files or directories you found. Did you find any flags?
Using robots.txt I found that there was a hidden directory /secret and the source for that page contained the flag CMSC389R-{fly_th3_sk1es_w1th_u5}.
Also, I found the /.git directory which contained the flag CMSC389R-{y0u_found_th3_g1t_repo}.

5. Did you find any other IP addresses associated with this website? What do they link to or where did you find them?
I found the IP address 142.93.117.193 and it links to an admin page. 

6. If you found any associated server(s), where are they located? How did you discover this?
The server with the IP 142.93.117.193 and the server with IP 142.93.117.193 are both located in New York and I found this information on Censys.

7. Which operating system is running on the associated server(s)? How did you discover this? 
The OS running on both servers is Ubuntu and I found this on Censys.

8.Did you find any other flags on your OSINT mission?
CMSC389R-{h1dden_fl4g_in_s0urce} - Found in source of home page
CMSC389R-{dns-txt-rec0rd-ftw} - DNS dumpster


### Part 2 (55 pts)

The first thing I did was write the python script and make sure it was working and iterating through the wordlist.  The next thing I did was begin running the script with potential usernames.  I tried runnig the script with "Kruegster1990","admin","fredkrueger" but these two were also unsuccessful.  Lastly, I tried "kruegster" which was the right username.  The password was Pokemon which made sense, since there were Pokemon references on his Twitter and Instagram.  I found the flight records in /home/flight_records.  Although all the flight records seemed like flags, I think the flight record that was most important was the flight record whose number was posted on Instagram and contained the flag CMSC389R-{c0rn3rstone-air-27670}.

