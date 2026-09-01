line1=["⬜","⬜","⬜"]
line2=["⬜","⬜","⬜"]
line3=["⬜","⬜","⬜"]
alphabets=["a","b","c"]
map=[line1,line2,line3]
position=input("enter a position:")
# now we have to see what is the input and fix the index according to the input given by user
alpha=alphabets.index(position[0].lower())
number=int(position[1])-1
map[alpha][number]="❌"
print(map)