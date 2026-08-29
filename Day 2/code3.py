age=int(input("\nEnter your age:"))
if age<18:
    print("\nMinor")
elif age>18 and age<60:
    print("\nAdult")
else:
    print("\nSenior Citizen")
# output
# Enter your age:22
# Adult
