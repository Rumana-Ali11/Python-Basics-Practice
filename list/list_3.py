numbers = [10, 45, 32, 67, 89, 23]             #Find largest and second largest number in a list
largest = max(numbers)
numbers.remove(largest)
second_largest = max(numbers)
print("Largest:", largest)
print("Second Largest:", second_largest)