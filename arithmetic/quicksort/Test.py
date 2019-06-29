
'''
    快速排序
    快速排序不稳定，时间复杂度为 O(nlogn)
'''
def quicksort(arr):
    if len(arr)<=1:
        return arr
    else:
        base=arr[0]
        before=[i for i in arr[1:] if i<=base]
        after=[i for i in arr[1:] if i>base]
        return quicksort(before)+[base]+quicksort(after)

if __name__ == '__main__':
    arr1=[61,2,45,1,856,15,686,3216,5,631,68,15,16,1,15,650,65,15,16,1]
    print(quicksort(arr1))