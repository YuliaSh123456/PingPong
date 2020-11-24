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
            except:
                print "Client aborted"
                break
            if data == "SHUTDOWN":
                conn.sendall("GOODBYE")
                break
            else:
                print data
                conn.send(data + data)

        conn.close()
        print conn
        print 'client disconnected'
    serv.close()


if __name__ == "__main__":
    main()
