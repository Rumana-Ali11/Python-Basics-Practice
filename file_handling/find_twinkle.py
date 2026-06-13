f=open("poem.txt")
content=f.read()
if ("Twinkle" in content.lower()):
    print("twinkle is present")
else:
    print("twinkle is not present")
f.close()