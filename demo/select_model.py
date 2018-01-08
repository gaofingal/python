import select,socket,sys
import queue

server = socket.socket()
server.bind(('localhost',9000))
server.listen(1000)


server.setblocking(False)


inputs = [server,]
outputs = []

readable,writeable,exceptional = select.select(inputs, outputs, inputs)
print(readable,writeable,exceptional)


server.accept()