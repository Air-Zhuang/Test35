'''==================(1)Python2 Python3 不同=========================='''

'''1、print成为函数'''

'''2、编码问题。Python3不再有Unicode对象，默认str就是unicode'''

'''3、除法变化。Python3除号返回浮点数'''

'''4、类型注解(type hint).帮助IDE实现类型检查'''
def hello(name:str) -> str:
    return 'hello'+name

'''5、优化的super()方便直接调用父类函数'''

'''6、高级解包操作。a,b,*rest=range(10)'''
a,b,*c=[1,2,3,4,5]
*x,y,z=[1,2,3,4,5]

'''7、限定关键字参数(以*分割，后面的参数传递必须要指定参数名)'''
def add(a,b,*,c):
    return a+b+c
print(add(1,2,c=3))

'''8、Python3重新抛出异常不会丢失栈信息(用raise from保留异常栈信息)'''
import shutil
def mycopy(source,dest):
    try:
        shutil.copy2(source,dest)
    except OSError: # python2 里 raise 会丢失原来的 traceback 信息
        raise NotImplementedError("automatic sudo injection") from OSError
mycopy('old','new')

'''9、一切返回迭代器 range,zip,map,dict.values,etc. are all iterators'''

'''==================(2)Python3 新增=========================='''

'''1、yield from链接子生成器'''

'''2、asyncio内置库, async/await 原生支持协程,支持异步编程'''

'''3、新的内置库 enum,mock,asyncio,ipaddress,concurrent.futures等'''

'''==================(3)Python3 改进=========================='''

'''1、生成的pyc文件统一放到__pycache__'''

'''2、一些内置库的修改。urllib,selector等'''

'''==================(4)Python2/3 兼容工具=========================='''

'''1、six模块'''

'''2、2to3等工具转换代码'''

'''3、__future__'''