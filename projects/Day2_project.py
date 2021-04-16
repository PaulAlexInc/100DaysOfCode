# Tip calculator

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))
tip_amount=bill * (tip/100)
total = bill+tip_amount
each_person_share= total/no_of_people
rounded_share = "{:.2f}".format(each_person_share)
print(f"Each person should pay: ${rounded_share}")