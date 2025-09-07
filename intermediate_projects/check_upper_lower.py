total = 0
text = input("Enter a text:")
upper = 0
lower = 0
for ch in text:
    if ch.upper():
        upper+=1
    elif ch.lower():
        lower+=1
print("the upper is ",upper)
print("the lower is ",lower)