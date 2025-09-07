#create while loop program that prints number from 18 to 2
#create control variable
number = 18
#create count variable and initialize with 0
count = 0
while number >= 0:
    # count the iteration
    count = count + 1
    # display the number with iteration
    print(f"the number in iteration {count} is {number}")
    number = number - 1
#print the total iteration
print(f"the total iteration is {count}")
