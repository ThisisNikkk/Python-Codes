def linear_search(list1,n,key):
    for i in range(0,n):
        if list1[i]==key:
            return i
    else:
        return -1
list1=[1,3,4,5,6,7,9]
key=5
n=len(list1)
val=linear_search(list1,n,key)
if val==-1:
    print("Element Not Found")
else:
    print("Element Found At Index",str(val))