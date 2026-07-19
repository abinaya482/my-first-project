import random 
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

print("====PASSWORD GENERATOR====")

length = int(input("Enter the length of the password: "))

password = generate_password(length)

print("\nGenerated paassword")

print(password)
