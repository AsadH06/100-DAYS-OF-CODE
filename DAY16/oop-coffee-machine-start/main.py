# ─────────────────────────────────────────────────────────────
#  main.py — Entry point of the OOP Coffee Machine
#
#  This file does one job: run the machine loop.
#  All the actual logic (menu, resources, payment) lives in
#  separate class files. This file just coordinates them.
#
#  Imports bring in the three class blueprints:
#    Menu        → knows what drinks are available
#    CoffeeMaker → knows the machine's resources and how to brew
#    MoneyMachine → knows how to handle payment
# ─────────────────────────────────────────────────────────────
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Instantiate one object from each class.
# Each object holds its own state (data) and behaviour (methods).
# These three objects talk to each other through the main loop below.
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


# ─────────────────────────────────────────────────────────────
#  coffee_machine()
#
#  The main control loop. Reads user input and delegates every
#  task to whichever object is responsible for it.
#
#  Notice: this function has almost no logic of its own.
#  It doesn't check ingredients, handle coins, or build menu strings —
#  it just asks the right object to do those things.
#  That's the point of OOP: responsibilities are separated.
# ─────────────────────────────────────────────────────────────
def coffee_machine():

    while True:
        # menu.get_items() builds the prompt string dynamically from
        # whatever drinks are currently in the Menu object's list.
        # If you add a new drink to Menu, the prompt updates automatically.
        choice = input(f"What would you like? ({menu.get_items()})").lower()

        if choice == "off":
            break   # exits the while True loop and ends the program

        elif choice == "report":
            # Each object reports only what it owns:
            # coffee_maker reports water/milk/coffee levels
            # money_machine reports profit collected
            coffee_maker.report()
            money_machine.report()

        else:
            # Step 1: Ask Menu if this drink exists → returns a MenuItem object or None
            coffee = menu.find_drink(choice)

            # find_drink() returns None for unknown inputs and prints its own error.
            # `continue` skips the rest of this loop iteration and re-prompts the user.
            if coffee is None:
                continue

            # Step 2: Ask CoffeeMaker if it has enough ingredients for this drink.
            # The MenuItem object (coffee) is passed in — CoffeeMaker reads its ingredients.
            if coffee_maker.is_resource_sufficient(coffee):

                # Step 3: Ask MoneyMachine to handle payment for this drink's cost.
                # coffee.cost reads the cost attribute directly from the MenuItem object.
                if money_machine.make_payment(coffee.cost):

                    # Step 4: Only if both checks pass, brew the coffee.
                    # CoffeeMaker receives the full MenuItem object so it knows
                    # exactly which ingredients to deduct and what name to print.
                    coffee_maker.make_coffee(coffee)


coffee_machine()