import random
names_string = input("Give me a list of names: ")
names = names_string.split(",")
random_int=random.randint(0,(len(names)-1))
print(f'{names[random_int]} is going to buy the meal today!')