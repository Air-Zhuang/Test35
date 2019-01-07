#用类的方法
class Averager(object):
    def __init__(self):
        self.series=[]
    def __call__(self, new_value):
        self.series.append(new_value)
        total=sum(self.series)
        return total/len(self.series)
avg=Averager()
print(avg(10))
print(avg(11))
print(avg(12))
print()
#用闭包的方式
def make_averager():
    series=[]   #这里使用和调用闭包中的series是因为series是可变的数据类型，如果不可变则报错
    def averager(new_value):
        series.append(new_value)
        total=sum(series)
        return total/len(series)
    return averager
avg2=make_averager()
print(avg2(10))
print(avg2(11))
print(avg2(12))
print()

#这个会报错,因为count=0和total=0为不可变数据类型
# def make_averager2():
#     count=0
#     total=0
#     def averager(new_value):
#         count+=1
#         total+=new_value
#         return total/count
#     return averager

#python3使用nonlocal解决如上问题
def make_averager2():
    '''nonlocal的作用是把变量标记为自由变量，即使在函数中为变量赋予新值了，也会变成自由变量'''
    count=0
    total=0
    def averager(new_value):
        nonlocal count,total
        count+=1
        total+=new_value
        return total/count
    return averager
avg3=make_averager2()
print(avg3(10))
print(avg3(11))
print(avg3(12))
print()