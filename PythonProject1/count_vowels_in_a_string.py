text = input('Enter text:')
count = 0
vowels = 'aeouiAEOUI'
for char in text:
    if char in vowels:
        count+=1
print('number of vowels ', count)