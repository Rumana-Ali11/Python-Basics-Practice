n = int(input("How many items? "))          #Create a dictionary from user input
d = {}
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value
print(d)