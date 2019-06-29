import time

class LogTime:
    def __call__(self, func):
        def _log(*args,**kwargs):
            beg=time.time()
            res=func(*args,**kwargs)
            print("use time:{}".format(time.time()-beg))
            return res
        return _log

class LogTime2:
    def __init__(self,use_int=False):   #实现了在装饰器中添加参数
        self.use_int=use_int
    def __call__(self, func):
        def _log(*args,**kwargs):
            beg=time.time()
            res=func(*args,**kwargs)
            if self.use_int:
                print("use time:{}".format(int(time.time()-beg)))
            else:
                print("use time:{}".format(time.time()-beg))
            return res
        return _log

@LogTime()
@LogTime2(use_int=True)      #这里要加括号(因为是用类实现装饰器)
def mysleep():
    time.sleep(1)

mysleep()