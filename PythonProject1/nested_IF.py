print("-----------------------------------")
age = int(input("Enter your age:"))
weight = int(input("Enter your weight:"))
if age > 20:
    if weight > 50:
        print("you are eligible to donate.")
    else:
        print("you are not eligible to donate.")
else:
    print("the age be greater than 21.")
    print("-----------------------------------")