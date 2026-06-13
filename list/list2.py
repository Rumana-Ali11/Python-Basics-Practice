numbers = [12, 7, 9, 18, 25, 30]                #Find even and odd numbers from a list
even = []
odd = []                
for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers:", even)
print("Odd numbers:", odd)