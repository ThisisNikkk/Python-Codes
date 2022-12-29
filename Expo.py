a=int(input("Enter The Number:"))
b=int(input("Enter The Power:"))
if b==0:
    print(1)
else:
    for i in range(1,b+1):
        result=a**i
    print(result)