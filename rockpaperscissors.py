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
play_again = True
while play_again:
  valid_choice = False
  while not valid_choice:
    choice = int(input("Type '0' for rock, '1' for paper, or '2' for scissors: "))
    if choice == 0 or choice == 1 or choice == 2:
      valid_choice = True
    else:
      print("Invalid choice. Try again.")
      
  comp_choice = random.randint(0,2)
  
  if choice == 0:
    print(rock)
  elif choice == 1: 
    print(paper)
  else:
    print(scissors)
  
  print(f"Computer Chose: {comp_choice}")
  if comp_choice == 0:
    print(rock)
  elif comp_choice == 1: 
    print(paper)
  else:
    print(scissors)
  
  if choice < comp_choice:
    print("You lose!")
  elif choice > comp_choice:
    print("You win!")
  else:
    print("Draw!")

  val = input("Would you like to play again? Type 'Yes' or 'No': ")
  if val.lower() == 'no':
    play_again = False
    print("Finished playing!")
    
    
  