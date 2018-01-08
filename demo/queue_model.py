import queue

q = queue.PriorityQueue()
q.put((-1,'a'))
q.put((2,'s'))
q.put((5,'v'))
q.put((3,'e'))
q.put((8,'f'))

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())