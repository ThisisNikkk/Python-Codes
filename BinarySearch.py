def bin_search(list1,n):
    low=0
    high=len(list1)-1
    mid=0
    while low<=high:
        mid=(high+mid)//2
        if list1[mid]<n:
            low=mid+1
        elif list1[mid]>n:
            high=mid-1
        else:
            return mid
    return -1
list1=[10,13,14,15,20,27,30]
n=15
val=bin_search(list1,n)
if val!=-1:
    print("Element is present at index",str(val))
else:
    print("Element is not present")