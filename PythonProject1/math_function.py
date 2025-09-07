#this program demonstrates the square function
import math
def main():
    #get a number
    loop = 'j'
    while True:
        number = float(input("Enter a number:"))
        if number == 0.0:
            break
        #get the square root of the number
        square_root = math.sqrt(number)
        #display the square root
        print(f"the square root of number is {number} is {square_root:2f}.")
#call the main function
main()