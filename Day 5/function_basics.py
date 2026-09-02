def my_first_function(): # a new function is always defined using the def keyword
    num1=int(input("Enter num1:"))
    num2=int(input("Enter num2:"))
    product=num1*num2
    sum=num1+num2
    if num1>num2:
        difference=num1-num2
    else:
        difference=num2-num1
    print(f"The sum, product, difference of the two numbers are as follows \nproduct:{product} \nsum:{sum} \ndifference:{difference} ")
my_first_function() # I'm calling the function here so that whatever is written inside the 
# function gets executed and the output is returned