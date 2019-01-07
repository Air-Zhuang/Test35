import functools

'''functools.reduce'''
def f(n):
    print(functools.reduce(lambda a,b:a*b,range(1,n+1)))
f(4)
print()

'''functools.partial'''
'''把一个函数的某些参数设置默认值，返回一个新的函数，调用这个新函数会更简单。'''
'''使用partial把一个两参数函数改编成需要单参数的可调用对象'''

triple=functools.partial(lambda a,b:a*b,3)
print(triple(7))
print(list(map(triple,range(1,10))))
print()

def tag(name,*content,cls=None,**attrs):
    '''生成一个或多个HTML标签'''
    if cls is not None:
        attrs['class']=cls
    if attrs:
        attr_str=''.join(' %s="%s"' % (attr,value)
                         for attr,value in sorted(attrs.items()))
    else:
        attr_str=''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name,attr_str,c,name) for c in content)
    else:
        return '<%s%s />' % (name,attr_str)
print(tag('br'))
print(tag('p','hello'))
print(tag('p','hello','world'))
print(tag('p','hello',id=33))
print(tag('p','hello','world',cls='sidebar'))
print(tag(content='testing',name='img'))
my_tag={'name':'img','title':'Sunset Boulevard','src':'sunset.jpg','cls':'framed'}
print(tag(**my_tag))
print()

'''----------------------------------------------------------------'''
print(tag)
picture=functools.partial(tag,'img',cls='pic-frame')
print(picture(src='wumpus.jpeg'))
print(picture)
print(picture.func)
print(picture.args)
print(picture.keywords)
print()

'''----------------------------------------------------------------'''
def showarg(*args, **kw):
    print(args)
    print(kw)
p1 = functools.partial(showarg, 1, 2, 3)
p1()
p1(4, 5, 6)
p1(a='python', b='itcast')
print()

p2 = functools.partial(showarg, a=3, b='linux')
p2()
p2(1, 2)
p2(a='python', b='itcast')
print()

'''functools.wraps'''#Test35-->decorate-->flucent_2wraps.py
'''使用装饰器时，被装饰后的函数其实已经是另外一个函数了,添加后由于函数名和函数的doc发生了改变，对测试结果有一些影响，例如:'''
def note(func):
    "note function"
    def wrapper():
        "wrapper function"
        print('note something')
        return func()
    return wrapper
@note
def test():
    "file function"
    print('I am file')
test()
print(test.__doc__)
print()
'''所以，Python的functools包中提供了一个叫wraps的装饰器来消除这样的副作用。例如：'''
def note(func):
    "note function"
    @functools.wraps(func)
    def wrapper():
        "wrapper function"
        print('note something')
        return func()
    return wrapper
@note
def test():
    "file function"
    print('I am file')
test()
print(test.__doc__)
print()
'''functools.total_ordering'''
'''7_5'''

'''functools.lru_cache'''
'''decorate.flucent_3lru_cache'''

'''functools.singledispatch'''
'''decorate.flucent_singledispatch'''
