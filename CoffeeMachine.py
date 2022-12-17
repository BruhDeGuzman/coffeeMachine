from data import *


water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]


def pay():
    print("Please insert coins.")
    global quarters, dimes, nickles, pennies, total_money
    quarters *= int(input("how many quarters?: "))
    dimes *= int(input("how many dimes?: "))
    nickles *= int(input("how many nickles?: "))
    pennies *= int(input("how many pennies?: "))
    total_money = quarters + dimes + nickles + pennies


def report(water, milk, coffee, money):
    return f"water: {water}ml\nmilk: {milk}ml\ncoffee: {coffee}g\nmoney: {money}$"


def espresso():
    global water, coffee
    water -= 50
    coffee -= 18
    print("here's your espresso. enjoy")
    return water, coffee


def latte():
    global water, milk, coffee
    water -= 200
    milk -= 150
    coffee -= 24
    print("here's your latte. enjoy")
    return water, milk, coffee


def cappuccino():
    global water, milk, coffee
    water -= 250
    milk -= 100
    coffee -= 24
    print("here's your cappuccino. enjoy")
    return water, milk, coffee


money = 0
while True:
    total_money = 0
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01

    order = input("What would you like? (espresso/latte/cappuccino): ")

    if order == "report":
        print(report(water, milk, coffee, money))

    elif order == "espresso":
        if water < 50:
            print("Sorry there is not enough water.")
        else:
            pay()
            if total_money < 1.50:
                print("Sorry that's not enough money. Money refunded.")
                money = 0
            elif total_money > 1.50:
                change = round(total_money - 1.50, 2)
                print(f"here's {change}$ in change.")
                espresso()
                money += 1.50

    elif order == "latte":
        if water < 200:
            print("Sorry there is not enough water.")
        else:
            pay()
            if total_money < 2.50:
                print("Sorry that's not enough money. Money refunded.")
                money = 0
            elif total_money > 2.50:
                change = round(total_money - 2.50, 2)
                print(f"here's {change}$ in change.")
                latte()
                money += 2.50

    elif order == "cappuccino":
        if water < 250:
            print("Sorry there is not enough water.")
        else:
            pay()
            if total_money < 3.00:
                print("Sorry that's not enough money. Money refunded.")
                money = 0
            elif total_money > 3.00:
                change = round(total_money - 3.00, 2)
                print(f"here's {change}$ in change.")
                cappuccino()
                money += 3.00

    elif order == "off":
        break





