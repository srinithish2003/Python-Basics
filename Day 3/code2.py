import random
# Generate a random integer (either 0 or 1)
random_side = random.randint(0, 1)
# Map 1 to Heads and 0 to Tails
if random_side == 1:
    print("Heads")
else:
    print("Tails")