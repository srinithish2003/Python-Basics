print("Thank you for choosing Python Pizza Deliveries!")
size = input("Enter the size of Pizza you want - ") # S, M, or L
add_pepperoni = input("Want Pepperoni?") # want pepperoni? Y or N
extra_cheese = input("Want Extra cheese?") # want extra cheese? Y or N

bill = 0

if size.lower() == "s":
    bill += 15
elif size.lower() == "m":
    bill += 20
elif size.lower() == "l":
    bill += 25

if add_pepperoni.lower() == "y":
    if size.lower() == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is: ${bill}.")
# output
# Thank you for choosing Python Pizza Deliveries!
# Enter the size of Pizza you want - l
# Want Pepperoni?y
# Want Extra cheese?y
# Your final bill is: $29.