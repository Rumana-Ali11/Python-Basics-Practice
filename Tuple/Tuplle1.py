t = (10, 20, 30, 40, 50)        #to print tuple
print(t)

t = (10, 20, 30, 40, 50)       #Find Length of a Tuple
print("Length:", len(t))

t = (1, 2, 3, 2, 4, 2)         #Count Occurrences of an Element
print(t.count(2))

t = (12, 45, 7, 89, 23)        #Find Maximum and Minimum Value
print("Maximum:", max(t))
print("Minimum:", min(t))  

t = ("Python", "Java", "C++")   #Iterate Through a Tuple
for item in t:
    print(item)
