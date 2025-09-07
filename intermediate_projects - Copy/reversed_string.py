from time import process_time_ns

text = input("Enter a text:")
reversed_text = ''
for ch in text:
    reversed_text = ch + reversed_text
print(reversed_text)