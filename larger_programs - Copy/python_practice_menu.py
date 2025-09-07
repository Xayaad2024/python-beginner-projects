import random
print('=====-PYTHON PRACTICE MENU======')
print('1.  odd or even checker')
print('2.  multiplication table (skip 5)')
print('3.  guess the number game.')
print('4.  Grade calculator.')
print('5.  prime number finder.')
print('6.  collatz sequence.')
print('7.  EXIT!')
while True:
    choice = input('\n Enter your choice (1-7):')
    if choice == '1':
        print('\n odd or even checker.')
        for num in range(1,21):
            if num % 2 == 0:
                print(f"{num} is even")
            elif num % 2 != 0:
                print(f"{num} is odd")

