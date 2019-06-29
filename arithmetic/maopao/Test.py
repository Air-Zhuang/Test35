
'''
    冒泡排序
    冒泡排序稳定，时间复杂度为 O(n2)
'''
str1=[10,9,8,7,6,5,4,3,2,1]
for i in range(len(str1)):
    for j in range(i+1,len(str1)):
        if str1[i]>=str1[j]:
            str1[i],str1[j]=str1[j],str1[i]
print(str1)