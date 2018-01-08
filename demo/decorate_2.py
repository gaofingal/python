# 完整版的装饰器

# 两层的装饰器
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2015-3-25')
# 调用函数
now();


def log_defence(action):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            if action == 'call':
                print('%s %s():' % (action ,func.__name__))
                return func(*args,**kwargs)
            else:
                print('illegal call function %s %s():' % (action, func.__name__))
        return wrapper
    return decorator

@log_defence(action='delete')
def now_defence():
    print('this is test function')

now_defence()