'''
内置的iter函数有以下作用
(1)检查对象是否实现了__iter__方法，如果实现了就调用它，获取一个迭代器。
(2)如果没有实现__iter__方法,但是实现了__getitem__方法，Python会创建一个迭代器，尝试按顺序(从索引0开始)获取元素。
(3)如果尝试失败,Python抛出TypeError异常,通常会提示"C object is not iterable"(C对象不可迭代),其中C的目标对象所属的类
'''

import re
import reprlib

RE_WORD=re.compile('\w+')
'''--------------------------'''    #没有实现迭代器
class Sentense2:
    def __init__(self,text):
        self.text=text
        self.words=RE_WORD.findall(text)
    def __getitem__(self, index):   #使Sentense的对象可以实现切片
        return self.words[index]
    def __len__(self):
        return len(self.words)
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
'''--------------------------'''    #两种方式生成迭代器
class Sentense:
    def __init__(self,text):
        self.text=text
        self.words=RE_WORD.findall(text)
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    def __iter__(self):
        return SentenceIterator(self.words)
class SentenceIterator:
    def __init__(self,words):
        self.words=words
        self.index=0
    def __next__(self):
        try:
            word=self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index+=1
        return word
    # def __iter__(self):
    #     return self
#上面两个class合并可写成 Sentense3，不过最好不要这么做，因为：
#为了"支持多种遍历",必须能从同一个可迭代的实例中获取多个独立的迭代器，而且各个迭代器能维护自身的内部状态，
#因此这一模式正确的实现方式是，每次调用iter(my_iterable)都新建一个独立的迭代器。这就是为什么这个实例需要定义SentenceIterator类
class Sentense3:
    def __init__(self,text):
        self.text=text
        self.words=RE_WORD.findall(text)
        self.index=0
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    def __iter__(self):
        return self
    def __next__(self):
        try:
            word=self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index+=1
        return word
'''--------------------------'''    #最好的方式
'''最好的方式，更符合Python习惯'''
class Sentence4:
    def __init__(self,text):
        self.text=text
        self.words=RE_WORD.findall(text)
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    def __iter__(self):
        '''只要Python函数的定义体中有yield关键字，该函数就是生成器函数。调用生成器函数时，
        会返回一个生成器对象。也就是说，生成器函数是生成器工厂。'''

        '''迭代时，for机制的作用与g=iter(gen_AB())一样，用于获取生成器对象，然后每次迭代时调用next(g)'''
        for word in self.words:
            yield word
'''--------------------------'''    #最好的方式，更懒惰，更省内存
class Sentence5:
    def __init__(self,text):
        self.text=text
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    def __iter__(self):
        # for match in RE_WORD.finditer(self.text):
        #     yield match.group()
        return (match.group() for match in RE_WORD.finditer(self.text))     #生成器表达式：与上面注释的两句效果一样

s=Sentence5("I'm air")
print(s)
for i in s:
    print(i)
print(list(s))