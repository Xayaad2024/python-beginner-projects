# this program is created by sentinel value
sum = 0
number = int(input("enter a number to ad (or enter -1 to stop it all):"))
while number != -1:
    sum+=number
    number = int(input("enter a number to ad (or enter -1 to stop it all)"))
print("the total of sum is "+str(sum))