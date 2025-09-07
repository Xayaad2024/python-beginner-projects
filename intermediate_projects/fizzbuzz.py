# for num in range(1,101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("fizzbuzz")
#     elif num % 3 == 0:
#         print("fizz")
#     elif num % 5 == 0:
#         print("buzz")
#     else:
#         print(num)
total = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        total+=i
print("sum",total)