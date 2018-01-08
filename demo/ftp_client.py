import socket

client = socket.socket()
client.connect(('localhost',9999))


while True:

    cmd = input(">>:").strip()
    client.send(cmd)
    send_size = client.recv(1024)
    receive_size = 0


    print()