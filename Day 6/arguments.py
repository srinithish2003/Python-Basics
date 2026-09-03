list=[10,20,30,40,50,60,70,40,50,60,70]
def calculate_avg(list):
    sum=0
    for number in list:
        sum+=number
    average=round((sum/len(list)),2)
    return f"the average of the list is {average}"
print(calculate_avg(list))