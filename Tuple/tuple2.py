#Store employee salaries in a tuple and count how many salaries are above ₹50,000
salaries = (45000, 60000, 55000, 40000, 75000, 30000)
count = 0
for salary in salaries:
    if salary > 50000:
        count += 1
print("Number of salaries above ₹50,000:", count)