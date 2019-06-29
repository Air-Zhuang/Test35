
def binary_search(list,searchNum):
    item=0
    low=0
    high=len(list)-1
    while low<=high:
        mid=(low+high)/2
        if list[mid]==searchNum:
            print('总共查询了%d次' % item)
            return mid
        else:
            item+=1
            if list[mid]<searchNum:
                low=mid+1
            elif list[mid]>searchNum:
                high=mid-1
    return None
if __name__ == '__main__':
    list1=[]
    for i in range(1000):
        list1.append(i)
    print(binary_search(list1, 499))
    print(binary_search(list1, 498))