import socket

server = socket.socket()
# 绑定要监听端口
server.bind(('localhost',6969))
# 监听
server.listen()
conn,addr = server.accept()

print(conn,addr)
data = conn.recv(1024)
print("recv:",data)
conn.send(data.upper())


server.close()