'''yield'''
# def gen_func():
#     #下面这段代码 1、可以产出值 2、可以接受值(调用方传递进来的值)
#     html=yield "http://www.baidu.com"
#     print(html)
#     yield 2
#     yield 3
#
# gen=gen_func()
# print(next(gen))
# print(gen.send("air1"))    #send方法可以传递值进入生成器内部,同时还可以重启生成器执行到下一个yield
# print(next(gen))
# # gen.throw(Exception,"self-defined Exception")     #主动抛出异常
# print()

'''yield from和yield区别'''
def g1(iterable):
    yield iterable
def g2(iterable):
    yield from iterable

for i in g1(range(3)):
    print(i)
for i in g2(range(3)):
    print(i)

'''
main():调用方  g1():委托生成器  gen:子生成器
yield from 会在调用方与子生成器之间建立一个双向通道

def g1(gen):
    yield from gen
def main():
    g=g1()
    g.send(None)
'''