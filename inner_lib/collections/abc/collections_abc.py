'''查看__all__的源码'''
'''
例如：Sequence协议(不可变数据类型)-->继承自(Reversible, Collection)
        Reversible(可反转)-->继承自Iterable(可迭代)-->继承自Iterable(元类)
        Collection-->继承自 Sized(元类,可获取长度), Iterable(元类), Container(元类,判断 x in list(a))
'''

from _collections_abc import __all__