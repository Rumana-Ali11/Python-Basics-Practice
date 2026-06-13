#Store marks of students in a set and count how many scored above 75
marks = {65, 78, 82, 90, 70, 88, 75}
count = 0
for mark in marks:
    if mark > 75:
        count += 1
print("Students scoring above 75:", count)