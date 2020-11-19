import socket


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 50000))
    client.send("Hello")
    from_srvr = client.recv(4096)
    client.close()
    print from_srvr


if __name__ == "__main__":
    main()