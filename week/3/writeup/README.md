Writeup 3 - OSINT II, OpSec and RE
======

Name: Tumie Hurd
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Tumie Hurd

## Assignment 3 Writeup

### Part 1 (100 pts)
Vulnerability 1: Weak passwords

The vulnerability of weak password can be remediated if the user chooses a stronger password.  NIST has a number of great suggestions for creating more complex passwords including using passphrases with longer lengths. They say that a passphrase with 6 words can me more effective than 10 character password mix of letters, numbers, and symbols. Also, the user should consider locking the account for a period of time (15-30 minutes) after a specified number of failed login attempts. This will help decrease the effectiveness of brute force attacks.

Vulnerability 2: Open Ports

Fred can use nmap to discover open ports to see which ports he has available and make sure unused ports are closed. He should also use a service such as Nessus to scan the ports and see the vulnerabilities associated with the open ports.   

Vulnerability 3: No intrusion detection

If a malicious person gains access to his server, there is no way to determine what someone did or even tell that someone was inside the system.  He can use a SIEM to review audit logs of the system or trigger alerts when there are unrecognized IPs or behaviors.  

