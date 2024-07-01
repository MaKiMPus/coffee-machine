from coffee_data import menu, resources
import numpy


def resource_check(order_ingredients):
    """Check resources"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry that is not enough {item}")
            return False
    return True


def process_coins():
    """prompt the user to insert coins."""
    print("please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    """Calculate the monetary value of the coins inserted."""
    totals = quarters + dimes + nickles + pennies
    return totals


def deducted_ingredient(drink_name, order_ingredients):
    #make coffee
    """deducted the ingredients from the coffee machine resources"""
    """tell the user 'Here is your {user_choice}'."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕ Enjoy!")

profit = 0

machine_on = True
while machine_on:
    # prompt user by asking "what would they like?"
    user_choice = input("What would you like? (espresso, cappuccino, latte): ").lower()

    # Turn off coffee machine by entering "off" to the prompt
    if user_choice == "off":
        """use “off” as the secret word to turn off the machine. end execution when this happens."""
        machine_on = False
    elif user_choice == "report":
        # print report
        """When the user enters “report” to the prompt, a report should be generated that shows the current resource values."""
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${profit}")
    else:
        drink = menu[user_choice]
        # print(drink)

        # Check resources sufficient?
        if resource_check(drink['ingredients']):
            payment = process_coins()
            # check transaction successful?
            """Check that the user has inserted enough money to purchase the drink"""
            """Inserted too much money, the machine should offer change."""
            if payment == drink['cost']:
                profit += drink['cost']
                deducted_ingredient(user_choice, drink['ingredient'])
            elif payment > drink['cost']:
                profit += drink['cost']
                change = round((payment - drink['cost']), 2)
                print(f"Here is ${change} in change.")
                deducted_ingredient(user_choice, drink['ingredients'])
            else:
                print("Sorry that's not enough money. Money refunded.")

