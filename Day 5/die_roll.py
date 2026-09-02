# Input: 
# Player 1 Name: Varshith
# Player 2 Name: Kelvin
# Output:
# Varshith rolls: [3, 6, 2, 5, 4] → Total: 20  
# Kelvin rolls: [4, 1, 6, 3, 2] → Total: 16  
# Winner: Varshith
import random 
def dice_battle(list1,list2):
    total1=0
    total2=0
    winner=''
    for i in range(5):
        list1.append(random.randint(1,6))
        list2.append(random.randint(1,6))
    for i in range(len(list1)):
        total1=total1+list1[i]
    for i in range(len(list2)):
        total2=total2+list2[i]
    if total1>total2:
        winner=player1
    else:
        winner=player2
    return winner
player1=input("\nEnter the name of player1:")
player2=input("\nEnter the name of player2:")

list1=[]
list2=[]
result=dice_battle(list1,list2)
print(f"{player1} rolls: {list1} {player2} rolls:{list2}")
print("\nThe winner is",result)
