numbers = [10, 20, 30, 40, 50]

def reverse_list(numbers):
    reversed_list = []

    for i in range(len(numbers) - 1, -1, -1):# -1 
        reversed_list.append(numbers[i])

    return reversed_list

print(reverse_list(numbers)) 