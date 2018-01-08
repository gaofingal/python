import socket
import os
import hashlib

server = socket.socket()
server.bind(('localhost',9999))

server.listen()

while True:
    conn,addr = server.accept()
    while True:
        data = conn.recv(1024)
        conn.send(data)
server.close()