registry2=[]

def register2(func):
    print('running register(%s)' % func)
    registry2.append(func)
    return func
@register2
def f():
    print('running f()')

print('running main()')
print('registry2 ->',registry2)
print()

'''创建一个装饰器工厂函数，把参数传给它，返回真正的装饰器，
    返回的装饰器才是应用到目标函数上的装饰器'''
registry=set()
def register(active=True):
    def decorate(func):
        print('running register(active=%s)->decorate(%s)' % (active,func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate
@register(active=False)
def f1():
    print('running f1()')
@register()
def f2():
    print('running f2()')
def f3():
    print('running f3()')

print('registry ->',registry)