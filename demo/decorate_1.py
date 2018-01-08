

def foo(bar):
    def wap(*args,**kwargs):
        print("this is decorate start")
        bar()
        print("this is decorate end")
    return wap


@foo
def bar():
    print("this is bar")
bar()

