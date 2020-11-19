import socket


def main():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('localhost', 50000))
    serv.listen(5)
    conn, addr = serv.accept()
    from_client = ''
    data = "Start"
    while data != "":
        data = conn.recv(4096)
        if not data:
            break
        from_client += data
        print from_client
        conn.send(from_client + from_client)
    conn.close()
    print 'client disconnected'


if __name__ == "__main__":
    main()
