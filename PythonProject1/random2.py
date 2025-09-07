#this program creates a dice rolling program
import random
MIN = 1
MAX = 6
def mai():
    gain = 'yes'
    while gain == 'y' or gain == 'Y':
        print("Rolling the dice.....")
        print("their value are:")
        print(random.randint(MIN,MAX))
        print(random.randint(MIN,MAX))
        gain = input("Enter y or Y to roll gain:")
#call the main function
mai()