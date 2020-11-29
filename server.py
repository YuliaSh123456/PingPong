import select, socket, sys, Queue

inputs = []
outputs = []
message_queues = {}
data_to_send = 0

def add_new_client(new_socket):
    connection, client_address = new_socket.accept()
    connection.setblocking(0)
    inputs.append(connection)
    #message_queues[connection] = Queue.Queue()


def handle_client_input(socket_to_read):
    try:
        data = socket_to_read.recv(1024)
    except socket.error, e:
        print "Client aborted " + str(e)

        if socket_to_read in outputs:
            outputs.remove(socket_to_read)

        inputs.remove(socket_to_read)
        socket_to_read.close()
        #del message_queues[socket_to_read]
        return False

    if data:
        global data_to_send
        data_to_send = data + data
        if socket_to_read not in outputs:
            outputs.append(socket_to_read)
    else:
        if socket_to_read in outputs:
            outputs.remove(socket_to_read)
        inputs.remove(socket_to_read)
        socket_to_read.close()
        #del message_queues[socket_to_read]

    return True


def handle_client_output(socket_to_write):
    global data_to_send
    if data_to_send == 0:
        return

    try:
        socket_to_write.send(data_to_send)
        data_to_send = 0
    except socket.error, e:
        print "Client aborted " + str(e)


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(0)
    server.bind(('localhost', 50000))
    server.listen(5)

    inputs.append(server)

    while inputs:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)

        for s in readable:
            if s is server:
                add_new_client(s)
            else:
                if not handle_client_input(s):
                    continue

        for s in writable:
            handle_client_output(s)

        for s in exceptional:
            inputs.remove(s)
            if s in outputs:
                outputs.remove(s)
            s.close()
            #del message_queues[s]


if __name__ == "__main__":
    main()
