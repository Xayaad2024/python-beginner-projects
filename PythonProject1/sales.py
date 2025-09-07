#create a pay based on sales commission
from calculate import commission


def main():
    sales = get_sales()
    advanced_pay = get_advanced_pay()
    commission_rate = determine_commmission_rate(sales)
    pay = sales * commission_rate - advanced_pay
    print(f"the pay of sales employee is {pay:2f}")
    #deteremine whether the pay is negative
    if pay < 0:
        print("sales person must repay the company")
def get_sales():
    sales = float(input("Enter monthly sales:"))
    return sales
def get_advanced_pay():
    advanced_pay = float(input("Enter advanced pay or 0;"))
    return advanced_pay
def determine_commmission_rate(sales):
    if sales < 1000:
        rate = 0.10
    elif sales >= 1000 and sales <= 14999.99:
        rate = 0.12
    elif sales >= 15000 and sales <= 17999.99:
        rate = 0.14
    elif sales >= 18000 and sales <= 21999.99:
        rate = 0.16
    else:
        rate = 0.18
    return rate
#call the main function
main()