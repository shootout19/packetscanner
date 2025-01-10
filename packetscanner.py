import socket

def scan_Ports(ip):
    for port in range(1, 1000): # scan first 1000 prots
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip,port))
        if result == 0:
            print(f"PORT {port} is OPEN")
        sock.close()

target_IP = "8.8.8.8" # Replace with Your target IP
scan_Ports(target_IP)