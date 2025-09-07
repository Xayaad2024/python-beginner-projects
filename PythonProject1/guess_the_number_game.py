import random
number = random.randint(1,20)
attempts = 0

while True:
    guess1 = int(input("Guess a number between one to twenty:"))
    attempts += 1
    if guess1 < number :
        print("too low")
    elif guess1 > number:
        print("too high")
    else:print(f"correct you guessed it in {attempts} tries.")
    break