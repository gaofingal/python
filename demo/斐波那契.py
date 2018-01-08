
def fib(max):
    n,a,b = 0, 0 ,1
    while(n<max):
        yield b
        a,b=b,b+a
        n += 1
    return 'done'


f = fib(10)

while True:
    try:
        x = next(f)
        print(x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
