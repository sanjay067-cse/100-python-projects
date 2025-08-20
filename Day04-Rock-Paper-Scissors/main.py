import random
# ASCII art of Rock , Paper , Scissors
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
#Storing ASCII art of rock, paper, scissors in a list
img = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if user_choice >=0 and user_choice <= 3 :
    print(f"You chose :\n {img[user_choice]}")

#Making computer to choose a random value from 0-2 using random.randint() function and printing it from the img list.
comp_choice = random.randint(0,2)
print(f"Computer chose :\n {img[comp_choice]} ")

#Displaying Invalid message and making the user lose if user chooses any no. other than 0,1 and 2
if user_choice <0 or user_choice >= 3 :
    print("You chose an Invalid number. You Lost!")

#Deciding winner according to the game rules
if user_choice == comp_choice :
    print("Match Draw!")

elif user_choice == 0 and comp_choice == 1 :
    print("You lost!")
elif user_choice == 0 and comp_choice == 2 :
    print("You Won!")

elif user_choice == 1 and comp_choice == 2 :
    print("You lost!")
elif user_choice == 1 and comp_choice == 0 :
    print("You Won!")

elif user_choice == 2 and comp_choice == 0 :
    print("You lost!")
elif user_choice == 2 and comp_choice == 1 :
    print("You Won!")
    