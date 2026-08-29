#Leap year code
year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
# output
# 2025
# Not leap year

# A different approach can also be followed for this problem, using multiple conditions in a single if statement, by avoiding nesting
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not leap year")

# output
#     2100
# Not leap year