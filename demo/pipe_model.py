from multiprocessing import Pipe,Process


def f(conn):
    conn.send([42,None,'hello'])
    conn.send([42,None,'hello2'])
    print(conn.recv())
    conn.close()

if __name__ == '__main__':

    parent_conn,child_conn = Pipe()

    p = Process(target=f,args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    print(parent_conn.recv())
    parent_conn.send("hello,i am father")
    p.join()