scores=input("Enter the student scores:").split()
for n in range(0, len(scores)):
    scores[n]=float(scores[n])
highest=0
# now i'm loping through the entires list to find which number is highest
for score in scores:
    if score>highest:
        highest=score
print(f'The highest score is {highest}.')
