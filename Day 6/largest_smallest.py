numbers = [45, 12, 89, 34, 67, 5, 100]

def find_difference(numbers):

    largest = numbers[0]
    smallest = numbers[0]
    for number in numbers:

        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
            
    difference = largest - smallest
    return difference

print(find_difference(numbers))