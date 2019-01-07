'''
with语句会设置一个临时的上下文，交给上下文管理器对象控制，并且负责清理上下文。
这么做能避免错误并减少样板代码，因此API更安全，而且更易于使用。
除了自动关闭文件之外，with块还有很多用途。
'''
import os

path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(path+'\\High_Level_Coding_python3\\file\\4_3.txt') as fp:
    src=fp.read(60)
print(len(src))
print(fp)
print(fp.closed,fp.encoding)
# fp.read(60)

'''
在使用@contextmanager装饰的生成器中，yield语句的作用是把函数的定义体分成两部分：
yield语句前面的所有代码在with块开始(即解释器调用__enter__方法时)执行，
yield语句后面的代码在with块结束时(即调用__exit__方法时)执行。
'''
import contextlib

class MyResource:
    # def __enter__(self):
    #     print('connect to resource')
    #     return self
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     print('close resource connection')
    def query(self):
        print('query data')
# with MyResource() as r:
#     r.query()

@contextlib.contextmanager
def make_myresource():
    print('connect to resource')
    yield MyResource()
    print('close resource connection')
'''================================================================================='''
@contextlib.contextmanager
def looking_glass():
    import sys
    original_write=sys.stdout.write
    def reverse_write(text):
        original_write(text[::-1])
    sys.stdout.write=reverse_write
    msg=''
    try:                                    #之前是__enter__
        yield 'JABBERWOCKY'
    except ZeroDivisionError:               #__exit__
        msg='Please DO NOT divide by zero!'
    finally:
        sys.stdout.write=original_write
        if msg:
            print(msg)

'''用于原地重写文件的上下文管理器'''
# import csv
#
# with inplace(csvfilename,'r',newline='') as (infh,outfh):
#     reader=csv.reader(infh)
#     writer=csv.writer(outfh)
#
#     for row in reader:
#         row+=['new','columns']
#         writer.writerow(row)