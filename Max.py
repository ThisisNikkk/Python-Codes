n=int(input("Enter number of element in list :"))
mylist=[]
print("Enter elements of the list:")
for i in range(n):
    a=int(input())
    mylist.append(a)
maximum=max(mylist)
minimum=min(mylist)
print("Maximum of the list is :",maximum)
print("Minimum Of the list is :",minimum)