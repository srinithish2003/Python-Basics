target = int(input())

total_sum = 0
for number in range(2, target + 1, 2):
    total_sum += number

print(total_sum)
# range(2, target + 1, 2) starts at 2, increments by 2 to get only even numbers, 
# and ends at target + 1 so that target itself is included if it is an even number.