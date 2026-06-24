# ─────────────────────────────────────────────
#  MENU — a nested dictionary
#  Outer key   : drink name (string)
#  Inner keys  : "ingredients" (dict of amounts) and "cost" (float)
#  Water/milk measured in ml, coffee in grams.
# ─────────────────────────────────────────────
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

# ─────────────────────────────────────────────
#  resources — tracks what's currently available in the machine.
#  "money" accumulates the revenue collected (in dollars).
#  Water/milk in ml, coffee in grams.
# ─────────────────────────────────────────────
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


# ─────────────────────────────────────────────
#  coffee_machine() — the main controller function.
#
#  All helper functions are defined *inside* this function so they share
#  the same scope. This means every inner function can read and modify
#  `resources` and `MENU` directly — no need to pass them as arguments.
#
#  Note on dictionary mutation vs reassignment:
#    resources['money'] += 10   → works without 'global' keyword
#                                  (we're modifying the dict's contents)
#    resources = {}             → would need 'global' keyword
#                                  (we'd be reassigning the variable itself)
# ─────────────────────────────────────────────
def coffee_machine():
    machine_is_on = True  # flag that keeps the main while-loop running


    # ─────────────────────────────────────────
    #  is_sufficient(drink)
    #
    #  Checks whether the machine has enough of every ingredient
    #  required for the chosen drink.
    #
    #  How it works:
    #    1. Drills into MENU[drink]["ingredients"] to get only the
    #       ingredients relevant to this drink (never touches "money").
    #    2. Loops through each required ingredient and compares
    #       the required amount to what's in `resources`.
    #    3. Returns False immediately on the first shortage — no point
    #       checking the rest once we already know we can't make the drink.
    #    4. Returns True only if every ingredient passes.
    # ─────────────────────────────────────────
    def is_sufficient(drink):
        menu = MENU[drink]["ingredients"]   # drill into the nested dict
        for ingredient in menu:
            # required amount <= available amount → OK, keep checking
            if menu[ingredient] <= resources[ingredient]:
                continue
            else:
                print(f"Sorry there is not enough {ingredient}")
                return False   # early exit — stops checking the rest
        return True


    # ─────────────────────────────────────────
    #  print_report()
    #
    #  Prints the current state of all machine resources.
    #  Formats each value with the correct unit:
    #    money  → dollar sign ($)
    #    coffee → grams (g)
    #    water, milk → millilitres (ml)
    # ─────────────────────────────────────────
    def print_report():
        for key in resources:
            if key == "money":
                print(f"{key}: ${resources[key]}")
            elif key == "coffee":
                print(f"{key}: {resources[key]}g")
            else:
                print(f"{key}: {resources[key]}ml")


    # ─────────────────────────────────────────
    #  process_coins(drink)
    #
    #  Handles the payment flow for a chosen drink.
    #
    #  Coin values:
    #    Quarter = $0.25 | Dime = $0.10 | Nickel = $0.05 | Penny = $0.01
    #
    #  Why round(..., 2) everywhere?
    #    Floating-point arithmetic in Python is imprecise at the binary
    #    level — e.g. 0.1 + 0.2 gives 0.30000000000000004.
    #    Rounding to 2 decimal places keeps dollar amounts clean.
    #
    #  Revenue logic:
    #    balance = total inserted - drink cost  (change to give back)
    #    total - balance = exactly the drink cost → added to machine's money
    #    This avoids storing overpayment as revenue.
    #
    #  Returns True if payment is sufficient, False otherwise.
    # ─────────────────────────────────────────
    def process_coins(drink):
        print("Please insert coins")
        q = int(input("How many quarters?: "))
        d = int(input("How many dimes?: "))
        n = int(input("How many nickels?: "))
        p = int(input("How many pennies?: "))

        # Calculate total inserted, rounded to avoid floating-point errors
        total = round(float(q*0.25 + d*0.10 + n*0.05 + p*0.01), 2)

        if total >= MENU[drink]["cost"]:
            balance = round(total - MENU[drink]["cost"], 2)  # change to return
            resources['money'] += round(total - balance, 2)  # only the drink cost goes in
            print(f"Here is ${balance} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded")
            return False


    # ─────────────────────────────────────────
    #  make_coffee(coffee)
    #
    #  Deducts the required ingredients from `resources` and
    #  confirms the drink is ready.
    #
    #  How it works:
    #    Loops through the drink's ingredient dict and subtracts
    #    each required amount from `resources`.
    #    This works cleanly because both dicts share the same keys
    #    (water, milk, coffee) — no key mismatch possible.
    # ─────────────────────────────────────────
    def make_coffee(coffee):
        ingredient = MENU[coffee]['ingredients']
        for key in ingredient:
            resources[key] -= ingredient[key]  # deduct each ingredient used
        print(f"Here is your {coffee}. Enjoy!")


    # ─────────────────────────────────────────
    #  Main loop — keeps the machine running until "off" is entered.
    #
    #  Input handling order:
    #    1. "off"            → shut the machine down
    #    2. "report"         → display current resource levels
    #    3. not in MENU      → guard against invalid drink names;
    #                          without this, MENU[user_choice] would
    #                          throw a KeyError for unknown inputs
    #    4. valid drink name → check ingredients → process payment → make coffee
    #
    #  .lower() on input ensures capitalisation doesn't break matching
    #  (e.g. "Latte", "LATTE", "latte" all work).
    # ─────────────────────────────────────────
    while machine_is_on:
        user_choice = input("What would you like to drink? (espresso/latte/cappuccino): ").lower()

        if user_choice == "off":
            machine_is_on = False                  # exits the while loop

        elif user_choice == "report":
            print_report()                         # show resource levels

        elif user_choice not in MENU:
            print("Enter a valid choice")          # guard against KeyError

        else:
            # Only proceed if ingredients are available AND payment succeeds
            if is_sufficient(user_choice):
                if process_coins(user_choice):
                    make_coffee(user_choice)


coffee_machine()