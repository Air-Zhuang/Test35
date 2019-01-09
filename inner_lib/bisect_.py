import bisect

'''使用二分法使一个序列一直维持已排序的状态'''
'''
insort_right=insort 
bisect_right=bisect
insort_left
bisect_left
'''
l=[]
bisect.insort(l,30)             #插入
bisect.insort(l,20)
bisect.insort(l,50)
bisect.insort(l,10)
bisect.insort(l,60)
print(l)
print(bisect.bisect(l,60))      #查找
print(bisect.bisect_left(l,60)) #查找