row = int(input("Enter number of row:"))
columns = int(input("Enter number of columns:"))
for i in range(1,row+1):
    for j in range(1, columns+1):
        print(f"{i*j:5},end=''")
    print()