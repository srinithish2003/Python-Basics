list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = []

def prime_list(list):
    for number in list:
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                result.append(number)
    return result

print(prime_list(list))