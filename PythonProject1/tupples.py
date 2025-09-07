students = ("qanyare","21","male")

print(students.count('qanyare'))
print(students.index('male'))
for x in students:
    print(x)

if 'qanyare' in students:
    print("yes he is available:")
else:
    print("he is not available")