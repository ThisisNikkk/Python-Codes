
a = int(input("Enter the number:"))
for i in range(1, a+1):
    c = 0
    for j in range(1, i+1):
        a = i % j
        if a == 0:
            c = c + 1

    if c == 2:
        print(i)
    else:
        i = i - 1

    i = i + 1