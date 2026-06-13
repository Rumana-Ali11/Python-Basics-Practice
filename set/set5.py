#Remove all duplicate values from a list and display the unique values in sorted order

numbers = [10, 20, 10, 30, 40, 20, 50, 30]
unique_numbers = sorted(set(numbers))
print(unique_numbers)