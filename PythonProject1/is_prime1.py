def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
start = int(input("Enter start of range:"))
end = int(input("Enter end of range:"))
prime = [n for n in range(start,end+1)if isprime(n)]
print("prime number:",prime)