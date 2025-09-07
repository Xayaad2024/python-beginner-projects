n = int(input('How many numbers:?'))
largest = None
for _ in range(n):
    num = float(input('Enter a number:?'))
    if largest is None or num > largest:
        largest = num
    print('largest number is ', largest)
