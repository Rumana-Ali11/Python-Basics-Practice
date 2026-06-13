marks = {               #Find student with highest marks
    "Ali": 85,
    "Sara": 92,
    "John": 78,
    "Aman": 95
}
highest = max(marks, key=marks.get)
print("Top Student:", highest)
print("Marks:", marks[highest])