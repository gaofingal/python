
class Foo(object):

    def eat(self):
        print('this is eat')


def yeild():
    print('this is yield')

a = Foo()

if hasattr(a,'eat1'):
    f = getattr(a,'eat')
    f()
else:
    setattr(a,'talk',yeild)
    a.talk()