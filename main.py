from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()

# menuitem1 = MenuItem()

coffee_maker = CoffeeMaker()

money_machine = MoneyMachine()




isTrue = True

while isTrue:
    choice=input(f"What would you like")
    if choice  == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        isTrue= False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
