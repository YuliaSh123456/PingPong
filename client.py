import socket


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 50000))

    data_to_send = ""

    print "Insert message: "
    while data_to_send != "Exit":
        data_to_send = raw_input()
        client.send(data_to_send)
        from_srvr = client.recv(4096)
        print from_srvr

    client.shutdown(socket.SHUT_RDWR)
    client.close()
    print "Good bye... "


if __name__ == "__main__":
    main()
