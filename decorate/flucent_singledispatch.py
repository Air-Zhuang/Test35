import html

def htmlize2(obj):
    content=html.escape(repr(obj))
    return '<pre>{0}</pre>'.format(content)

print(htmlize2(1))
print(htmlize2([1,2,3]))
print(htmlize2("1"))
print()

'''python3.4新增的functools.singledispatch装饰器可以把整体方案拆分成多个模块
    使用@singledispatch装饰的普通函数会变成泛函数：
    根据第一个参数的类型，以不同方式执行相同操作的一组函数'''
from functools import singledispatch
from collections import abc
import numbers

@singledispatch
def htmlize(obj):
    content=html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)
def _(text):    #专门函数的名称无关紧要
    content=html.escape(text).replace('\n','<br>\n')
    return '<p>{0}</p>'.format(content)
@htmlize.register(numbers.Integral) #为每个需要特殊处理的类型注册一个函数。numbers.Integral是int的虚拟超类
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)
@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner='</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>'+inner+'</li>\n</ul>'

print(htmlize({1,2,3}))
print(htmlize(abs))
print(htmlize('airair \n airairair'))
print(htmlize(42))
print(htmlize(['alpha',66,{3,2,1}]))