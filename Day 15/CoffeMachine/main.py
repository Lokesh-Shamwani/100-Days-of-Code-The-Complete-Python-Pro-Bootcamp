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

MONEY = 0
RESOURCE_ENOUGH = False
MAKE_COFFEE = False
QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01


def ask_user():
    """asks user about their choice and return the input value"""
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return user_choice


def resource_report():
    """To print resource and money coffee machine have"""
    global MONEY
    for key in resources:
        print(f"{key}: {resources[key]}")

    print(f"Money: ${MONEY}")


def compare_ingredients(desired_coffee, ingredient):
    """to check quantity of each desired ingredient """
    if resources[ingredient] >= MENU[desired_coffee]["ingredients"][ingredient]:
        return True
    else:
        print(f"Sorry there is not enough {ingredient}")
        return False


def check_resource_sufficient(desired_coffee):
    """to check overall resource is available or not"""
    milk = False
    water = False
    coffee = False
    if desired_coffee == "espresso":
        milk = True
        water = compare_ingredients(desired_coffee, "water")
        coffee = compare_ingredients(desired_coffee, "coffee")

    elif desired_coffee == "latte":

        milk = compare_ingredients(desired_coffee, "milk")
        water = compare_ingredients(desired_coffee, "water")
        coffee = compare_ingredients(desired_coffee, "coffee")

    elif desired_coffee == "cappuccino":
        milk = compare_ingredients(desired_coffee, "milk")
        water = compare_ingredients(desired_coffee, "water")
        coffee = compare_ingredients(desired_coffee, "coffee")
    else:
        print("Invalid Choice entered")

    if milk and water and coffee is True:
        return True
    else:
        return False


def proceed_choice(user_choice):
    """to proceed user's choice and decide if making desired coffee is possible or not"""
    global RESOURCE_ENOUGH
    global MAKE_COFFEE
    if user_choice == "off":
        RESOURCE_ENOUGH = False
    elif user_choice == "report":
        resource_report()
        coffee_machine()
    elif user_choice == 'espresso':
        RESOURCE_ENOUGH = check_resource_sufficient(user_choice)
    elif user_choice == "latte":
        RESOURCE_ENOUGH = check_resource_sufficient(user_choice)
    elif user_choice == "cappuccino":
        RESOURCE_ENOUGH = check_resource_sufficient(user_choice)
    else:
        print(f"Invalid input {user_choice}")
        MAKE_COFFEE = False

    if RESOURCE_ENOUGH is True and user_choice != "off":
        MAKE_COFFEE = True
    else:
        MAKE_COFFEE = False


def process_coins(desired_coffee):
    """to handle the transaction, i.e. collecting coins, returning change"""
    global QUARTERS, DIMES, NICKLES, PENNIES

    price_of_coffee = MENU[desired_coffee]["cost"]
    print("Please insert coins.")
    quarters_coins = int(input("how many quarters?: "))
    dimes_coins = int(input("how many dimes?: "))
    nickles_coins = int(input("how many nickles?: "))
    pennies_coins = int(input("how many pennies?: "))
    monetory_value = ((QUARTERS * quarters_coins) + (DIMES * dimes_coins) + (NICKLES * nickles_coins) + (PENNIES * pennies_coins))
    if monetory_value < price_of_coffee:
        print("Sorry that's not enough money. Money refunded.")
        coffee_machine()
    elif monetory_value >= price_of_coffee:
        change = monetory_value - price_of_coffee
        return change


def make_coffee(desired_coffee):
    """to make coffee from the available resources"""
    global MONEY
    price_of_coffee = MENU[desired_coffee]["cost"]
    MONEY += price_of_coffee

    if desired_coffee == "espresso":
        resources["water"] -= MENU[desired_coffee]["ingredients"]["water"]
        resources["coffee"] -= MENU[desired_coffee]["ingredients"]["coffee"]
    elif desired_coffee == "latte":
        resources["milk"] -= MENU[desired_coffee]["ingredients"]["milk"]
        resources["water"] -= MENU[desired_coffee]["ingredients"]["water"]
        resources["coffee"] -= MENU[desired_coffee]["ingredients"]["coffee"]

    elif desired_coffee == "cappuccino":
        resources["milk"] -= MENU[desired_coffee]["ingredients"]["milk"]
        resources["water"] -= MENU[desired_coffee]["ingredients"]["water"]
        resources["coffee"] -= MENU[desired_coffee]["ingredients"]["coffee"]


def coffee_machine():

    user_choice = ask_user()
    if user_choice != "off":
        proceed_choice(user_choice)
        if MAKE_COFFEE is True:
            change = process_coins(user_choice)
            print(f"Here is ${round(change, 2)} in change.")
            make_coffee(user_choice)
            print(f"Here is your {user_choice} ☕️. Enjoy!")
            coffee_machine()

    elif user_choice == "off":
        print("Good Bye!")


coffee_machine()
