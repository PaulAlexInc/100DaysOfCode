from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

def highest_bid(auction):
  highest=0
  winner=""
  for name in auction:
    bid_amt=auction[name]
    if bid_amt > highest:
      highest=bid_amt
      winner=name
  print(f"{winner} is the highest bidder with a bid of ${highest}")


to_continue=True
auction = {}
while to_continue:
  name=input("What is your name?: ")
  bid=int(input("What's your bid?: $"))


  auction[name] = bid
  choice=input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  if choice=="no":
    to_continue=False
    highest_bid(auction)
  if choice=="yes": 
    clear()
