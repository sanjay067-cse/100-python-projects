# Printing ASCII art for treasure box
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_or_right = input("You have came to a road splitting into two directions. Type 'left' or 'right' to go into that direction: ")

#Converting the user input to Title case using title() function
if left_or_right.title() == "Right" :
    print("GAME OVER")

elif left_or_right.title() == "Left"  :
    swim_or_wait = input("Well Done! You chose the right direction and now you came to a river.So you want to 'swim' or 'wait'?: ")
    if swim_or_wait.title() == "Swim" :
        print("GAME OVER")
    elif swim_or_wait.title() == "Wait" :
        door = input("Well Done! You have passed the dangerous river.\nNow you have came into a house which has three doors. Red, Yellow and Blue.\nTreasure is inside one of the door.\nChoose the door color you want to open: ")
        if door.title() == "Red" :
            print("GAME OVER")
        elif door.title == "Blue" :
            print ("GAME OVER")
        elif door.title() == "Yellow" :
            print("Congratulations! You found the treasure.")
        else :
            print("Oops! Wrong Input")

#Displaying wrong input message to user if any direction other than 'left' or 'right' is chosen
else :
    print("Oops! Wrong Input")
    