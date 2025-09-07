# break
# continue
# pass
from importlib.metadata import pass_none

# break
while True:
    name = input("Enter your name:")
    if name != '':
        break

        # continue
phone_number = '123_456_789'
for i in phone_number:
    if i == '_':
        continue
    else:
        print(i,end='')

# pass
for i in range(1,21):
    if i == 13:
        continue
    else:
        print(i)
