# -*- coding: UTF-8 -*-

'''
杨辉三角形
'''
list1=[1,1]
for i in range(2,15):
    temp=[]
    for j in range(len(list1)+1):
        if j==0:
            temp.append(1)
        elif j!=0 and j!=len(list1):
            temp.append(list1[j-1]+list1[j])
        elif j==len(list1):
            temp.append(1)
    list1=temp
    print(temp)