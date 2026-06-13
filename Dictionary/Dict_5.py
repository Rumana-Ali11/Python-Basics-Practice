fav_language = {}               #Store 3 Friends' Favorite Languages
for i in range(3):
    name = input("Enter name: ")
    lang = input("Enter language: ")
    fav_language[name] = lang
print(fav_language)