#!/usr/bin/env python3
import socket

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
conn, addr = server_socket.accept()
print('Connected to', addr)
    
# ready to send and receive messages
data = conn.recv(1024)
msg = data.decode('utf-8')
print("Got msg ", msg)

res = evaluateQuery(msg)

msg = "RESULT " + res

conn.sendall(msg.encode())
conn.close()
