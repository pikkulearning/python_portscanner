import socket

target = "172.19.64.1"

def portscan(port: int):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

print(portscan(80))