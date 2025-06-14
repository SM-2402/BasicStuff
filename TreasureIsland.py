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
print("You're at a cross road. Where do you want to go?\n")
decision_1=input('Type "left" or "right"\n').lower() 
if decision_1 == "left": 
    print("You've come to a lake. There is an island in the middle of the lake.\n")
    decision_2=input('Type "wait" to wait for the boat. Type "swim" to swim across.\n').lower()
    if decision_2 == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue.")
        decision_3=input("Which colour do you choose?\n").lower()
        if decision_3 == "yellow":
            print("You found the treasure. You win")
        elif decision_3 == "red":
            print('Yov\'ve entered a room of fire. Game over')
        elif decision_3 == "blue":
            print('You\'ve entered a room of beasts. Game over')
        else:
            print("You choose an invalid door. Game Over.")
    elif decision_2 == "swim":
        print("Attacked by a trout. Game Over.")
    else:
        print("Invalid input")
elif decision_1 == "right":
    print("Fall into a hole. Game Over.")
else:
    print("Invalid input")
    