import socket


def main():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('localhost', 50000))
    serv.listen(5)
    conn, addr = serv.accept()
    data = "Start"
    while data != "":
        data = conn.recv(4096)
        print data
        conn.send(data + data)
    conn.close()
    print 'client disconnected'
    serv.close()


if __name__ == "__main__":
    main()
