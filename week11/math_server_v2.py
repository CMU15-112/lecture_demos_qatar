#!/usr/bin/env python3
import socket
import select

def evaluateQuery(query):
    return str(eval(query))

SERVER_HOST = '127.0.0.1'  #   Use 0.0.0.0 for any network interface
SERVER_PORT = 15112        # Port to listen on (non-privileged ports are > 1023)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# not necessary, for convenience
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)

print('Listening on port %s ...' % SERVER_PORT)

   # Wait for client connections

watched_sockets = [server_socket]


while True:
    # ready to send and receive messages
    read_sockets, _, _ = select.select(watched_sockets, [], [] )
    for s in read_sockets:
        if s == server_socket:
            conn, addr = s.accept()
            watched_sockets.append(conn)
            print('Connected to', addr)
        else:
            data = s.recv(1024)
            if len(data) > 0:
                msg = data.decode('utf-8')
                print("Got msg ", msg)
                res = evaluateQuery(msg)
                msg = "RESULT " + res
                s.sendall(msg.encode())
            else:
                break
    
conn.close()
