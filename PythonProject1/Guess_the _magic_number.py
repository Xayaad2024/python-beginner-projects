#guess the magic number
import random
number = random.randint(1,100)
while True:
    Guess = int(input("Enter your guess:"))
    if Guess == number:
        print("yes you number is "+str(number))
        break
    elif Guess > number:
        print("your guess is too high.")
    else:
        print("your guess is too low.")

