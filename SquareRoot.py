def mySqrt(x):
    r = x
    precision = 10 ** (-10)

    while abs(x - r * r) > precision:
        r = (r + x / r) / 2

    return r
print("Enter The Number Which You Have To Find The Square Root")
a=float(input())
print("Answer Is",mySqrt(a))