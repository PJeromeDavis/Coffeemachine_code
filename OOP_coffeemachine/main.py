from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffeemaker=CoffeeMaker()
money_machine= MoneyMachine()
menu= Menu()
print(menu.get_items())
coffeemaker.report()
money_machine.report()
is_on= True
while is_on:
  options = menu.get_items()
  choice = input(f"What would you like? {options}")
  if choice == "off":
    is_on = False
  elif choice == "report":
    coffeemaker.report()
    money_machine.report()
  else :
    drink = menu.find_drink(choice)
    drink_cost = drink.cost
    coffee_available = coffeemaker.is_resource_sufficient(drink)
    if coffee_available:  
      print(f"Your drink costs {drink_cost}.\nPlease make payment.")
      payment=money_machine.make_payment(drink_cost)
      if payment:
          make_coffee = coffeemaker.make_coffee(drink)  
    else:
      print("Please notify maintenance.")
      