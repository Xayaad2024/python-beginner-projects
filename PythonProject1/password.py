password = "xayaad2024"
again = 'try again'
while True:
    my_password = input("Enter the password:")
    if my_password == password:
        print(f"DONE")
        print("do you want to enter another time:")
    else:
        print("INCORRECT TRY AGAIN!")