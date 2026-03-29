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
    "money": 0
}



def coffee_machine():
    machine_is_on = True


    def is_sufficient(drink):
        menu = MENU[drink]["ingredients"]
        for ingredient in menu:
            if menu[ingredient] <= resources[ingredient]:
                continue
            else:
                print(f"Sorry there is not enough {ingredient}")
                return False
        return True

    def print_report():
        for key in resources:
            if key == "money":
                print(f"{key}: ${resources[key]}")
            elif key == "coffee":
                print(f"{key}: {resources[key]}g")
            else:
                print(f"{key}: {resources[key]}ml")

    def process_coins(drink):
        print("Please insert coins")
        q = int(input("How many quarters?: "))
        d = int(input("How many dimes?: "))
        n = int(input("How many nickels?: "))
        p = int(input("How many pennies?: "))
        total = round(float(q*0.25 + d*0.10 + n*0.05 + p*0.01), 2)
        if total >= MENU[drink]["cost"]:
            balance = round(total - MENU[drink]["cost"], 2)
            resources['money'] += round(total - balance, 2)
            print(f"Here is ${balance} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded")
            return False


    def make_coffee(coffee):
        ingredient = MENU[coffee]['ingredients']
        for key in ingredient:
            resources[key] -= ingredient[key]
        print(f"Here is your {coffee}. Enjoy!")




    while machine_is_on:
        user_choice = input("What would you like to drink? (espresso/latte/cappuccino): ").lower()

        if user_choice == "off":
            machine_is_on = False
        elif user_choice == "report":
            print_report()
        elif user_choice not in MENU:
            print("Enter a valid choice")
        else:
            if is_sufficient(user_choice):
                if process_coins(user_choice):
                    make_coffee(user_choice)


coffee_machine()


"""
Coffee Machine - Key Concepts & Logic

Project Structure

All functions defined inside coffee_machine() — they share scope and can access resources and MENU directly without passing them as arguments every time


Global Dictionary Mutation
python
resources['money'] += 10  # works without global keyword
resources = {}  # this would need global keyword
Modifying dictionary contents vs reassigning the variable entirely — Python treats these differently

is_sufficient(drink)
python
menu = MENU[drink]["ingredients"]  # drill into nested dict
if menu[ingredient] <= resources[ingredient]:  # required <= available

Loops through drink's ingredients only — money key in resources never comes up because it's not in MENU[drink]["ingredients"]
Returns False immediately on first insufficient ingredient — no point checking rest


process_coins(drink)
python
total = round(float(q*0.25 + d*0.10 + n*0.05 + p*0.01), 2)
balance = round(total - MENU[drink]["cost"], 2)
resources['money'] += round(total - balance, 2)

round(..., 2) used everywhere because floating point arithmetic is imprecise in Python — 0.1 + 0.2 gives 0.30000000000000004 without rounding
total - balance = exactly the drink cost — clean way to add only what's owed to machine


make_coffee(drink)
python
for key in ingredient:
    resources[key] -= ingredient[key]

Loops through ingredients and deducts — simple but elegant
Works because both dicts share the same keys (water, milk, coffee)


While Loop Structure
python
if user_choice == "off":        # exit
elif user_choice == "report":   # report
elif user_choice not in MENU:   # invalid input guard
else:                           # valid drink flow

Invalid input guard added with not in MENU — without this, passing unknown drink to MENU[drink] would throw a KeyError
continue statements at the end were unnecessary — loop continues naturally anyway


Edge Cases Handled

.lower() on input → handles capitalisation
not in MENU check → handles invalid drink names
round(..., 2) → handles floating point errors
return False early in is_sufficient → no unnecessary checks after failure
"""