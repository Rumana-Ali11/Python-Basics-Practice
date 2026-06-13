#Take 5 Numbers from User and Store in a Set
s = set()
for i in range(5):
    num = int(input("Enter a number: "))
    s.add(num)
print(s)