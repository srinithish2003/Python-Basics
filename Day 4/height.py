student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# here we are replicating the sum() function using for loop
total_height = 0
for height in student_heights:
    total_height += height

# here we are replicating the len() function using for loop
number_of_students = 0
for student in student_heights:
    number_of_students += 1

# using inbuilt function to round off the average height
average_height = round(total_height / number_of_students)

print(f"total height = {total_height}")
print(f"number of students = {number_of_students}")
print(f"average height = {average_height}")