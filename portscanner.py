import socket
import sys

def main():
    target = sys.argv[1]
    port = sys.argv[2]
    send_ICMP(target)
    send_TCP(target,port)


def send_ICMP(target):
    sock_ICMP = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    sock_ICMP.settimeout(3)
    sock_ICMP.sendto(b'\x08\x00\xf5\xfc\x01\x01\x01\x02', (target, 0))
    try:
        result=sock_ICMP.recv(255)
    except socket.timeout:
        print(f"Target ({target}) is not active...")
        exit(0)
    sock_ICMP.close()
    print(f"Target ({target}) is active!")


def send_TCP(target,port):
    sock_TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock_TCP.connect_ex((target, int(port)))
    sock_TCP.close()
    if result == 0:
        print(f"Port{port} is open!")


if __name__ == "__main__":
    main()
