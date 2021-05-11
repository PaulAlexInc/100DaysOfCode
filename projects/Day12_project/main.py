#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# import random
# from art import logo
# print(logo)

# def check(user_guess, guess):
#   global to_continue
#   if user_guess < guess:
#     print("Too low\nGuess again.")
#   elif user_guess > guess:
#     print("Too high\nGuess again.")
#   else:
#     to_continue=False
#     print(f"You got it! The answer was {guess}")


# print("Welcome to the number guessing game!!!")
# guess=random.randint(1,100)
# print(guess)
# user_mode=input("Which mode do you want. Type 'easy' or 'hard' : ").lower()
# user_guess=int(input("Guess a number between 1 and 100 : "))

# def mode(user_mode):
#   if user_mode=="easy":
#     return 10
#   else:
#     return 5




# to_continue=True
# n=mode(user_mode)
# while to_continue:
#   check(user_guess,guess)
#   if to_continue==True and n!=0:
#     print(f"You have {n} attempts remaining to guess the number")
#     user_guess=int(input("Make a guess : "))
#     n=n-1
#   elif n==0:
#     print("You've run out of turns")
#     to_continue=False

####################Alternate method####################





import random
from art import logo
print(logo)

#Global constant
EASY_TURNS = 10
HARD_TURNS = 5


def check(user_guess,guess, turns):
  """checks answer agains guess, returns number of turns"""
  if user_guess < guess:
    print("Too low\nGuess again.")
    return turns-1
    
  elif user_guess > guess:
    print("Too high\nGuess again.")
    return turns-1
  else:
    
    print(f"You got it! The answer was {guess}")

def mode():
  user_mode=input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
  if user_mode=="easy":
    return EASY_TURNS
  else:
    return HARD_TURNS



  

def game():
  print("Welcome to the number guessing game!!!")
  print("I'm guessing a number between 1 and 100 : ")
  guess=random.randint(1,100)
  print(guess)
  turns=mode()

  
  user_guess=0
  while user_guess!=guess:
    print(f"You have {turns} turns remaining")
    user_guess=int(input("Make a guess : "))
    turns=check(user_guess,guess, turns)
    if turns==0:
      print("You've run out of guesses, you lose")
      return
    
game()