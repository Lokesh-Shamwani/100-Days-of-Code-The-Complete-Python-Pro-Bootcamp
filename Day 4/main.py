import random

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

#Write your code below this line 👇

arr = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if not( user_choice < 0 or user_choice > 2) :

  print(arr[user_choice])
  computer_choice = random.randint( 0, len(arr)-1 )
  print("Computer choose:")
  print(arr[computer_choice])
  
  if user_choice == 0 and computer_choice == 2:
    print("You Win!")
  elif user_choice == 2 and computer_choice == 0:
    print("You Lose!")
  elif user_choice > computer_choice:
    print("You Win!")
  elif computer_choice > user_choice:
    print("You Lose!")
  elif user_choice == computer_choice:
    print("It's a Draw")
else:
    print("you typed an invalid number, you lose! ")





