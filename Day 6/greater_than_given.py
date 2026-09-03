numbers = [10, 25, 40, 15, 60, 30]
# this function takes two arguments
def find_greater_numbers(numbers, value):
    result = []

    for number in numbers:
        if number > value:
            result.append(number)

    return result

print(find_greater_numbers(numbers, 25))