
n=int(input("enter a number:"))
for i in range(2, n):               #prime no 2,3,5,7......
    if n % i == 0:
        print("not prime no:")
        break
    else:
        print("prime no:")
