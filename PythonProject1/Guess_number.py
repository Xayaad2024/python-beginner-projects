import random
number = random.randint(1,100)
guess3 = int(input("Enter a number between 1,100:"))
if guess3 == number:
    print("correct!")
else:print("incorrect! the number was",number)
