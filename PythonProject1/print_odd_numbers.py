start = int(input("start:"))
end = int(input('End:'))
for num in range(start,end +1):
    if num % 2 != 0:
        print(num,end='')