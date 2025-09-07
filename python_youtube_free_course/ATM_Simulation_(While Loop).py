from bdb import Breakpoint
from random import choice
balance = 0
while True:
    print("\n---------------ATM MENU-------------")
    print("1.  check your balance.")
    print("2.  deposit.")
    print("3.  withdraw. ")
    print("4.   exit.")
    choice = input("Enter your choice:")
    if choice == '1':
        print(f"your balance is ${balance}")
    elif choice == '2':
        amount = float(input("Enter the deposit amount:"))
        balance +=amount
        print(f"successful deposit")
    elif choice == '3':
        amount = float(input("Enter withdrawal amount:"))
        if amount <= balance:
            balance -= amount
            print(f"successful withdrawal")
        else:
             print("unsufficient fund!")
    elif choice == '4':
        print(f"thank for using our ATM")
        break
    else:
        print("INVALID NUMBER.")
