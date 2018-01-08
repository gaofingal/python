import socket
import select
import queue

server = socket.socket()
server.bind(('localhost',90000))

server.listen(1000)

server.setblocking(False) #不阻塞

msg_dic = {}

inputs = []
outputs = []

while True:
    readable,writeable,exceptional = select.select(inputs, outputs, inputs)

    for r in readable:
        if r is server:#表示新来了一个链接
            conn,addr = server.accept()
            print('来了新连接',addr)
            inputs.append(conn) #因为这个新建立的连接还没有数据发过来，现在就接受的话程序会报错，要想实现这个客户端发数据过来时，server能知道，就让select再监测这个conn
            msg_dic[conn] = queue.Queue() #初始化一个队列，后面要返回个这个客户端数据
        else:
            data = r.recv(1024)
            print('收到的数据',data)
            msg_dic[r].put(data)
            outputs.append(r) #放到返回的连接队列里

    for w in writeable: #要返回给客户端的连接列表
        data_to_client = msg_dic[w].get()
        w.send(data_to_client) #返回给客户端的源数据
        outputs.remove(w)

    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)
        del msg_dic[e]
