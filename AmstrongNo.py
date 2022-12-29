num=int(input("Enter The Number To Be Checked: "))
sum=0
temp=num
while temp>0:
    digit = temp%10
    sum += digit**3
    temp //= 10
if num == sum:
    print("This is an amstrong number",num)
else:
    print("This is not an amstrong number",num)