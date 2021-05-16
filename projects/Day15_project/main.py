from supplies import resources, MENU
from datetime import datetime
from art import logo

WATER = resources["water"]
MILK = resources["milk"]
COFFEE = resources["coffee"]
MONEY = 0
quarter = 0.25
dime = 0.10
nickel = 0.05
penny = 0.01

def greeting():
    now = datetime.now()
    current_time = int(now.strftime(("%H")))

    if (current_time>= 00) and (current_time < 12):
        return "Good Morning"
    elif (current_time >= 12) and (current_time < 17):
        return "Good Afternoon"
    elif (current_time >= 17):
        return "Good Evening"

def process_coins():
    print("Please insert coins.")
    no_of_quarter = int(input("How many quarters?:"))
    no_of_dime = int(input("How many dimes?:"))
    no_of_nickel = int(input("How many nickels?:"))
    no_of_penny = int(input("How many pennies?:"))
    total = quarter*no_of_quarter + dime*no_of_dime + nickel*no_of_nickel + penny*no_of_penny
    return total

def espresso (milk, water, coffee):
    global MONEY, WATER, COFFEE
    water_reqd = MENU["espresso"]["ingredients"]["water"]
    coffee_reqd = MENU["espresso"]["ingredients"]["coffee"]
    cost = MENU["espresso"]["cost"]
    if water < water_reqd:
        print("Sorry there is not enough water.")
    elif coffee < coffee_reqd:
        print("Sorry there is not enough coffee.")
    else:
        amt_received=process_coins()
        if amt_received < cost:
            print("Sorry that's not enough money. Money refunded.")
        else:
            WATER -= water_reqd
            COFFEE -= coffee_reqd
            change = amt_received-cost
            MONEY += amt_received-change
            print("Here is ${:.2f} in change".format(change))
            print("Here is your espresso ☕️. Enjoy!")


def latte(milk, water, coffee):
    global MONEY, WATER, COFFEE, MILK
    water_reqd = MENU["latte"]["ingredients"]["water"]
    coffee_reqd = MENU["latte"]["ingredients"]["coffee"]
    milk_reqd =  MENU["latte"]["ingredients"]["milk"]
    cost = MENU["latte"]["cost"]
    if water < water_reqd:
        print("Sorry there is not enough water.")
    elif coffee < coffee_reqd:
        print("Sorry there is not enough coffee.")
    elif milk < milk_reqd:
        print("Sorry there is not enough coffee.")
    else:
        amt_received = process_coins()
        if amt_received < cost:
            print("Sorry that's not enough money. Money refunded.")
        else:
            WATER-=water_reqd
            COFFEE-=coffee_reqd
            MILK-=milk_reqd
            change = amt_received - cost
            MONEY += amt_received - change
            print("Here is ${:.2f} in change".format(change))
            print("Here is your latte ☕️. Enjoy!")

def cappuccino(milk, water, coffee):
    global MONEY, WATER, COFFEE, MILK
    water_reqd = MENU["cappuccino"]["ingredients"]["water"]
    coffee_reqd = MENU["cappuccino"]["ingredients"]["coffee"]
    milk_reqd = MENU["cappuccino"]["ingredients"]["milk"]
    cost = MENU["cappuccino"]["cost"]
    if water < water_reqd:
        print("Sorry there is not enough water.")
    elif coffee < coffee_reqd:
        print("Sorry there is not enough coffee.")
    elif milk < milk_reqd:
        print("Sorry there is not enough coffee.")
    else:
        amt_received = process_coins()
        if amt_received < cost:
            print("Sorry that's not enough money. Money refunded.")
        else:
            WATER -= water_reqd
            COFFEE -= coffee_reqd
            MILK -= milk_reqd
            change = amt_received - cost
            MONEY += amt_received - change
            print("Here is ${:.2f} in change".format(change))
            print("Here is your cappuccino ☕️. Enjoy!")

def report(milk, water, coffee):
    print(f"Water: {WATER}ml")
    print(f"Milk: {MILK}ml")
    print(f"Coffee: {COFFEE}mg")
    print(f"Money: ${MONEY}")

power_on = True
while power_on:
    print(logo)
    print(greeting())
    print("**** MENU ****\n1.Espresso : $1.5\n2.Latte : $2.5\n3.Cappuccino : $3.0\n**************")
    order = input("What would you like to have? (espresso/latte/cappuccino ): ").lower()
    order_dictionary = {
            "espresso" : espresso,
            "latte" : latte,
            "cappuccino" : cappuccino,
            "report" : report
        }
    if order == "espresso" or order == "latte" or order == "cappuccino" or order == "report":
        users_choice=order_dictionary[order]
        users_choice(milk=MILK, water=WATER, coffee = COFFEE)
    elif order == "off":
        print("Turning off...")
        power_on = False






