#this program will check if the number is prime
number = int(input("Enter a number to check if it is number or not:"))
if number % 2 != 0 and number / number == 0:
    print("it is prime number ",number)
else:
    print("it is not a prime number "+str(number))