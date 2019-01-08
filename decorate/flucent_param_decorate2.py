import time

DEFAULT_FMT='[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT):     #装饰器工厂
    def decorate(func):
        def clocked(*_args):
            t0=time.time()
            _result=func(*_args)
            elapsed=time.time()-t0
            name=func.__name__
            args=','.join(repr(arg) for arg in _args)
            result=repr(_result)
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorate
@clock()    #这里必须加()
def snooze1(seconds):
    time.sleep(seconds)
for i in range(3):
    snooze1(.123)
print()
@clock('{name}:{elapsed}s')
def snooze2(seconds):
    time.sleep(seconds)
for i in range(3):
    snooze2(.123)
print()
@clock('{name}((args)) dt={elapsed:0.3f}s')
def snooze3(seconds):
    time.sleep(seconds)
for i in range(3):
    snooze3(.123)
print()