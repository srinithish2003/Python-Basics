numbers = [10, 50, 30, 80, 20]

def find_min(numbers):
    minimum = numbers[0]

    for number in numbers:
        if number < minimum:
            minimum = number

    return minimum

print(find_min(numbers))