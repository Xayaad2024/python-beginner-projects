import random
import string
def generator_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars)for _ in range(length))
    return password
# Example usage
length = int(input("Enter password length:"))
print("generated password is ",generator_password(length))
