x=int(input("Enter Test1 Marks: "))
y=int(input("enter test2 marks: "))
z=int(input("enter test3 marks: "))
if x>z and y>z:
    print(x,y)
elif y>x and z>x:
    print(y,z)
elif z>x and x>y:
    print(z,x)
else:
    print("Error")


