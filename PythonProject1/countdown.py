import time

second = int(input("Enter countdown time in seconds:"))
for i in range(second,1,-1):
    print(i)
    time.sleep(1)
    print("time's up!")