import random
import string

def generate_password(length, strength):
    strong = string.ascii_letters + string.digits + string.punctuation
    medium = string.ascii_letters + string.digits
    weak = string.ascii_letters
    if strength == "strong":
        password = ''.join(random.choice(strong) for i in range(length))
        return password
    elif strength == "medium":
        password = ''.join(random.choice(medium) for i in range(length))
        return password
    elif strength == "weak":
        password = ''.join(random.choice(weak) for i in range(length))
        return password
    else:
        print("enter valid strength")

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        strength = (input("Enter the desired Strength of the password: "))
        if length <= 0:
            print("Please enter a valid positive length.")
            return

        password = generate_password(length, strength)
        print("Generated Password:", password)

    except ValueError:
        print("Please enter a valid number for the password length.")


main()