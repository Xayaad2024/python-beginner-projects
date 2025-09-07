age = int(input("HOW OLD ARE YOU?:"))
if age == 100:
    print("you are century old.")
elif age >= 22:
    print("you are an adult.")
elif age < 0:
    print("you still haven't been born.")
else:
    print("you are a child.")