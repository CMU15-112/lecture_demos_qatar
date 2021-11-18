#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 15112        # The port used by the server

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

query = input("type your query: ")

client_socket.sendall(query.encode())
response = client_socket.recv(1024)

print('Received', response.decode())