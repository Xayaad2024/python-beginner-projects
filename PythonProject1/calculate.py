# this program calculates commission of sales person
#create while loop control variable
keep_going = "yes"
#create while loop condition
while keep_going =="yes":
    #prompt the user to enter the sales and com_rate
    sales = float(input("Enter the sales per week:"))
    commission_rate = float(input("Enter the commission rate:"))
    #calculate the commission of sales?
    commission = sales * commission_rate
    #display the output of sales commission
    print(f"the sales coommission is {commission:.2f}")
    #let user to enter another sales
    keep_going = input("Do you want to calculate another sales: Enter yes/no")