import socket
import os


server = socket.socket()
server.bind(('localhost',9999))
server.listen()

while True:
    conn,addr = server.accept()
    print("new conn:",addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print("客户端已经断开")
            break
        print("执行指令")
        cmd_res = os.popen(data.decode()).read()
        if len(cmd_res) == 0:
            cmd_res = 'cmd has no output'

        conn.send(str(len(cmd_res.encode())).encode('utf-8'))
        conn.send(cmd_res.encode('utf-8'))
        print('send done')

server.close()