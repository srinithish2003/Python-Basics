districts_of_TN=["Tirunelveli","Madurai","Erode","Salem","Karur"]
print(districts_of_TN[4]) #indexing in lists by using the index number
print(districts_of_TN[-2]) # reverse indexing starts counting from the end of the list 
districts_of_TN[-2]="Vellore"
print(districts_of_TN[-2])
districts_of_TN.append("Chennai") # add a element to the existing list
districts_of_TN.extend(["Kovai","Tanjore"]) # add multiple elements to the existing list
print(districts_of_TN)
