file=open("info.txt",'r')
for line in file:
    result=line.title()
    print(result)
file.close()
