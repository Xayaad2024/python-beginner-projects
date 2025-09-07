temp = int(input("what is the temperature outside :"))
if not(temp >= 0 and temp <= 30):
    print("the temperature is not good today.")
    print("Do not go outside.")
elif not (temp < 0 or temp > 30):
    print("the temperature is not good today.")
    print("Do not go outside.")
