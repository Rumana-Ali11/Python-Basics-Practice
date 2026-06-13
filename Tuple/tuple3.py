#input a number from the user and print its index if found
t = (10, 20, 30, 40, 50)
num = int(input("Enter a number: "))
if num in t:
    print("Index =", t.index(num))
else:
    print("Number not found in tuple")