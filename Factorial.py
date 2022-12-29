def factorialnum(n):
    fact=1
    x=2
    while fact<=n:
        print(fact,end=" ")

        fact = fact * x
        x += 1
n = 100
factorialnum(n)