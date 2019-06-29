
'''
    选则排序
    选择排序不稳定，时间复杂度为 O(n2)
'''
def find_small_index(arr):
    small=arr[0]
    small_index=0
    for i in range(1,len(arr)):
        if arr[i]<small:
            small=arr[i]
            small_index=i
    return small_index
def sortoperation(arr):
    new_arr=[]
    for i in range(len(arr)):
        new_arr.append(arr.pop(find_small_index(arr)))
    return new_arr

b=[98,52,1,324,1,321,5,8,4,621,32,168,4,20,3,546,2,32,6]
print(sortoperation(b))