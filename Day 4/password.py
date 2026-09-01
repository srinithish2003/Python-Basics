import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
n_letters = int(input("How many letters would you like in your password?\n"))
n_symbols = int(input("How many symbols would you like?\n"))
n_numbers = int(input("How many numbers would you like?\n"))

password_list = []

# select random letters
for char in range(n_letters):
    password_list.append(random.choice(letters))
# select random symbols
for char in range(n_symbols):
    password_list.append(random.choice(symbols))
# select random numbers
for char in range(n_numbers):
    password_list.append(random.choice(numbers))

# Shuffle all characters so they aren't in predictable order
random.shuffle(password_list)
# Combine the character list into a single string
password = "".join(password_list) # the double quotes creates a new string and after that 
# we are joining created password to this new string

print(f"Here is your password: {password}")