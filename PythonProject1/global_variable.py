#create global variable using assignment statement
number = 100
print(f"display the value of the variable outside {number}")
def main():
    global number
    number = 200
    print(f"display the value of the variable inside {number}")
main()
print(f"display the value of the variable outside {number}")