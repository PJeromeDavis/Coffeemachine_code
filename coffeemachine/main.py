MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficient(order):
    for item in MENU[order]["ingredients"]:
        if resources[item]<=MENU[order]["ingredients"][item]:
                return False
    return True

def coffee(order):

    for item in MENU[order]["ingredients"]:
        resources[item]=(resources[item]-MENU[order]["ingredients"][item])
    x=MENU[order]["cost"]
    return resources

def change(user_pay,coffee_cost):
    return (user_pay-coffee_cost)
coffee_available=True
while coffee_available==True:
    coffee_order=input("What would you like? espresso/latte/cappuccino :")
    coffee_money=MENU[coffee_order]["cost"]
    coffee_available=is_resource_sufficient(order=coffee_order)
    if coffee_available==True:
        print(f"Your {coffee_order} costs ${coffee_money}.")
        penny=int(input("How much pennies do you want to insert?"))
        nickel=int(input("How much nickels do you want to insert?"))
        dime=int(input("How much dimes do you want to insert?"))
        quarter=int(input("How much quarters do you want to insert?"))
        user_money=((1*penny)+(5*nickel)+(10*dime)+(25*quarter))*0.01
        if user_money < coffee_money:
            print("Insufficent amount. Money refunded.")
        else:
            resources = coffee(order=coffee_order)
            print(resources)
            balance_change=change(user_pay=user_money, coffee_cost = coffee_money)
            print(f"Here is your {coffee_order} and here is your change of ${balance_change}")
    else:
        print(f"Sorry {coffee_order} not available")