import random
import string
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if (
            any(char.islower() for char in password)
            and any(char.isupper() for char in password)
            and any(char.isdigit() for char in password)
            and any(char in string.punctuation for char in password)
        ):
            break
    return password
if __name__ == "__main__":
    while True:
        try:
            password_length = int(input("Enter the desired password length: "))
            if password_length <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    generated_password = generate_password(password_length)
print("Generated Password:", generated_password)
