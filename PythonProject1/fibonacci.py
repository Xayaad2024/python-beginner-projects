def fibonacci(n):
    a ,b = 0 , 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a,b=b,a+b
    return sequence
n = int(input("Enter how many fibonacci number to generate:"))
print(fibonacci(n))