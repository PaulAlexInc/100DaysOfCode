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
rps=[rock,paper,scissors]
player_choice = int(input("What do you choose? Type 0 for Rock 1 for Paper or 2 for Scissors.\n"))
if player_choice>2 or player_choice<0:
  print("Invalid number, you lose")
  exit(0)
player = rps[player_choice]
print(player)

#computer_choice = rps[random.randint(0,2)] OR
computer_choice = random.choice(rps)
print(f"Computer chose:\n {computer_choice}")

if (player_choice==0):
  if(computer_choice==rock):
    print("Draw") 
  elif(computer_choice==paper):
    print("You lose")
  else:#scissors
    print("You win")
elif (player_choice==1):
  if(computer_choice==rock):
    print("You win") 
  elif(computer_choice==paper):
    print("Draw")
  else:#scissors
    print("You lose")
else:
  if(computer_choice==rock):
    print("You lose") 
  elif(computer_choice==paper):
    print("You win")
  else:#scissors
    print("Draw")

   
