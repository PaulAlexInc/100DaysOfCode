from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

is_on = True
while is_on:
    order_name = input(f"What would you like? ({menu.get_items()}):").lower()
    if order_name=="off":
        is_on=False
    elif order_name=="report":
        coffeemaker.report()
        moneymachine.report()
    else:
        drink = menu.find_drink((order_name))
        if(order_name in menu.get_items()):

            if coffeemaker.is_resource_sufficient(drink)==True:
                if moneymachine.make_payment(drink.cost) == True:
                    moneymachine.profit += drink.cost
                    coffeemaker.make_coffee(drink)



