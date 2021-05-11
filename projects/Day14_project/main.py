import random
from art import logo,vs
from game_data import data
# from replit import clear
print(logo)

# compare the followers for a and b
def compare_followers(CompareA, AgainstB, user_guess):
  
  if CompareA['follower_count'] > AgainstB['follower_count']:
    more_followers='A'
  elif CompareA['follower_count'] < AgainstB['follower_count']:
    more_followers='B'
  else:
    more_followers=user_guess
  
  return more_followers

# Randomly choose an item from the list for a
CompareA=random.choice(data)
# Randomly choose an item from the list for b. b!=a
score = 0
to_continue=True
while to_continue:

  AgainstB=CompareA #Preventing repetitions
  while AgainstB==CompareA:
    AgainstB=random.choice(data)

  
  print(f"Compare A: {CompareA['name']}, {CompareA['description']}, {CompareA['country']}.")
  print(vs)
  print(f"Against B: {AgainstB['name']}, {AgainstB['description']}, {AgainstB['country']}.")
  
  #*******************for testing*******************
  print(f"A : {CompareA['follower_count']}")
  print(f"B :: {AgainstB['follower_count']}")
  #*******************for testing*******************

  #Ask user who has more followers
  user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
  highest_follower_no = compare_followers(CompareA, AgainstB, user_guess)

  #compare user guess with the answer
  if user_guess == highest_follower_no:
    score +=1
    CompareA=AgainstB
    # clear()
    print(f"You're right! Current score: {score}")
  else:
    # clear()
    print(f"Sorry, that's wrong. Final score: {score}")
    to_continue=False
# if user guess is correct,increment score, assign b to a, choose randomly for b again. repeat process until user choice is wrong