import os
import time


def ping(host):

    response = os.system("ping -c 1 " + host +  " > /dev/null 2>&1")
    if response == 0:
        return True
    else:
        return False

host = "192.168.1.92"   




for i in range(3600):

    output = os.popen("ping -c 1 " + host).read()

    if "time=" in output:
        ping_ms = output.split("time=")[1].split("ms")[0]
        print("El host " + host + "respondio al ping con un timepo de " + ping_ms + "ms")

    else:
        print("El host " + host + "no respondio al ping")

    time.sleep(10)        





