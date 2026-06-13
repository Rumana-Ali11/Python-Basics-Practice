text = input("Enter a string: ")            #Count vowels in a string using dictionary
vowels = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
}
for i in text.lower():
    if i in vowels:
        vowels[i] += 1
print(vowels)