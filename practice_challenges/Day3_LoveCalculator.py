print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

c1=0
c2=0
name_added = name1.lower()+name2.lower()
c1+=name_added.count("t")
c1+=name_added.count("r")
c1+=name_added.count("u")
c1+=name_added.count("e")

c2+=name_added.count("l")
c2+=name_added.count("o")
c2+=name_added.count("v")
c2+=name_added.count("e")

total = int(str(c1)+str(c2))

if (total < 10) or (total > 90):
  print(f"Your score is {total}, you go together like coke and mentos.")
elif (total >= 40) and (total <= 50):
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")

