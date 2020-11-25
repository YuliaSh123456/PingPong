import socket


def main():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('localhost', 50000))
    serv.listen(5)
    while True:
        conn, addr = serv.accept()
        print 'Client from address: {} '.format(addr)
        data = "Start"
        while data != "":
            try:
                data = conn.recv(4096)
            except socket.error, e:
                print "Client aborted "+str(e)
                break

            if data != "":
                print data
                conn.send(data + data)

        conn.close()
        print 'client disconnected'
    serv.close()


if __name__ == "__main__":
    main()
