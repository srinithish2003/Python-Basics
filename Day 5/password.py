import random
import string

def generate_password(length):
    if length < 4:
        return "Password is too short. Minimum length must be 4."
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice("@#$%^&*!()")

    required = [upper, lower, digit, special]
    all_chars = string.ascii_letters + string.digits + "@#$%^&*!()"
    remaining = [random.choice(all_chars) for _ in range(length - 4)] #generate (length - 4) random characters from the full set of allowed characters
    #this is because (upper,lower,digit,specail char) is already chosen 

    password_list = required + remaining #concatenation of the remaining and required list
    random.shuffle(password_list)

    return ''.join(password_list)
length = int(input("\nEnter desired password length: "))
password = generate_password(length)
print("\nGenerated Password:", password)
