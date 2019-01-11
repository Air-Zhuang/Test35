import multiprocessing as mp
import threading as td
import time,os

'''tarena'''
# def worker(sec,name):
#     for i in range(3):
#         time.sleep(sec)
#         print(name)
# if __name__ == '__main__':
#     p=mp.Process(target=worker,args=(2,),kwargs={'name':'Air'},name="Process1")
#     p.start()
#     print("获取进程名称",p.name)
#     print("获取进程PID",p.pid)
#     print("进程alive状况",p.is_alive())
#     p.join()

'''完整的线程和进程创建对比代码'''

# def job(a,d):
#     print('aaaaa')

# if __name__ == '__main__':
#     t1 = td.Thread(target=job,args=(1,2))
#     p1 = mp.Process(target=job,args=(1,2))
#     t1.start()
#     p1.start()
#     t1.join()
#     p1.join()
'''
存储进程输出Queue          (效率一般，广泛灵活)
    Queue的功能是将每个核或线程的运算结果放在队里中， 等到每个线程或核运行完毕后再从队列中取出结果， 
    继续加载运算。原因很简单, 多线程调用的函数不能有返回值, 所以使用Queue存储多个线程运算的结果
'''
# def job(q):
#     res=0
#     for i in range(1000):
#         res+=i+i**2+i**3
#     q.put(res)    #queue
#
# if __name__=='__main__':
#     q = mp.Queue()
#     p1 = mp.Process(target=job,args=(q,))
#     p2 = mp.Process(target=job,args=(q,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     res1 = q.get()
#     res2 = q.get()
#     print(res1+res2)

'''
进程池Pool
    进程池Pool()和map():
        有了池子之后，就可以让池子对应某一个函数，我们向池子里丢数据，池子就会返回函数返回的值。 
        Pool和之前的Process的不同点是丢向Pool的函数有返回值，而Process的没有返回值。
    自定义核数量:
        Pool默认大小是CPU的核数，我们也可以通过在Pool中传入processes参数即可自定义需要的核数量
    apply_async():
        apply_async()中只能传递一个值，它只会放入一个核进行运算，但是传入值时要注意是可迭代的，
        所以在传入值后需要加逗号, 同时需要用get()方法获取返回值
    apply():
        apply()和apply_async()一样，但没有返回值
    总结:
        Pool默认调用是CPU的核数，传入processes参数可自定义CPU核数 
        map() 放入迭代参数，返回多个结果 
        apply_async()只能放入一组参数，并返回一个结果，如果想得到map()的效果需要通过迭代
'''
# def job(x):
#     return x*x
# def multicore():
#     pool = mp.Pool()
#     res = pool.map(job, range(10))
#     print(res)
#     res = pool.apply_async(job, (2,))
#     print(res.get())                                                # 用get获得结果
#     multi_res = [pool.apply_async(job, (i,)) for i in range(10)]    # 迭代器，i=0时apply一次，i=1时apply一次等等
#     print([res.get() for res in multi_res])                         # 从迭代器中取出
#     pool.close()
#     pool.join()
# if __name__ == '__main__':
#     multicore()

'''
共享内存shared memory           (效率较高，需要注意进行互斥操作)
    Shared Value:
        我们可以通过使用Value数据存储在一个共享的内存表中。
    Shared Array:
        在Python的mutiprocessing中，有还有一个Array类，可以和共享内存交互，来实现在进程之间共享数据。
'''
# value1 = mp.Value('i', 0)
# value2 = mp.Value('d', 3.14)
#
# array = mp.Array('i', [1, 2, 3, 4])
'''
线程通讯：Pipe                   (效率一般，多用于父子进程)
    fd1,fd2=Pipe(duplex=True)
    功能：创建管道
    参数：默认表示双向管道，如果设置为False则为单向管道
    返回值：表示管道的两端，如果是双向管道 都可以读写，如果是单向管道 则fd1只读 fd2只写
    fd.recv()
    功能：从管道读取信息
    返回值：读取到的内容
    *如果管道为空则阻塞
    fd.send(data)
    功能：向管道写入内容
    参数：要写入的内容
    *可以发送Python数据类型
'''

'''
进程锁Lock
'''
# def job(v, num, l):
#     l.acquire() # 锁住
#     for _ in range(5):
#         time.sleep(0.1)
#         v.value += num # 获取共享内存
#         print(v.value)
#     l.release() # 释放
#
# def multicore():
#     l = mp.Lock() # 定义一个进程锁
#     v = mp.Value('i', 0) # 定义共享内存
#     p1 = mp.Process(target=job, args=(v,1,l)) # 需要将lock传入
#     p2 = mp.Process(target=job, args=(v,3,l))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#
# if __name__ == '__main__':
#     multicore()

'''
Semaphore()

sem=Semaphore(num)
功能：创建信号量
参数：信号量初始值
返回：信号量对象

sem.acquire()   将信号量数量减一   信号量为0会阻塞
sem.release()   将信号量数量加一
sem.get_value() 获取当前信号量的值
'''
#创建信号量
sem=mp.Semaphore(3)
def fun():
    print("进程%d等待信号量" % os.getpid())
    #消耗一个信号量
    sem.acquire()
    print("进程%d消耗信号量" % os.getpid())
    time.sleep(3)
    sem.release()
    print("进程%d添加信号量" % os.getpid())
if __name__ == '__main__':
    jobs=[]
    for i in range(4):
        p=mp.Process(target=fun)
        jobs.append(p)
        p.start()
    for i in jobs:
        i.join()
    print(sem.get_value())