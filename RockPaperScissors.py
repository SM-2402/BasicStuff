rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
index = int(input(print("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors")))
selection = [rock,paper,scissors]
computer_selection = random.choice(selection)

if index == 0 and computer_selection == selection[2] or index == 2 and computer_selection == selection[1] or index == 1 and computer_selection == selection[0]:
    print(selection[index])
    print("computer chose:")
    print(computer_selection)
    print("You win!")
elif computer_selection == selection[index] :
    print(selection[index])
    print("computer chose:")
    print(computer_selection)
    print("Draw")
else:
    print(selection[index])
    print("computer chose:")
    print(computer_selection)
    print("You loose!")
    