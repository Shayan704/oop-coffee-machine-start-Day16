from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import art
menu = Menu()

# menuitem1 = MenuItem()

coffee_maker = CoffeeMaker()

money_machine = MoneyMachine()



isTrue = True

while isTrue:
    print(art)
    choice=input(f"What would you like?{menu.get_items()}\t")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        print("Thank you for visiting.")
        isTrue= False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
