# ─────────────────────────────────────────────────────────────
#  coffee_maker.py — CoffeeMaker class
#
#  Models the physical machine: it holds the ingredient resources
#  and knows how to check them, report them, and consume them
#  when making a drink.
#
#  OOP concept — Encapsulation:
#  The resources dict lives *inside* this object. Nothing outside
#  directly edits self.resources — they call methods on this object
#  and let it manage its own state.
# ─────────────────────────────────────────────────────────────
class CoffeeMaker:
    """Models the machine that makes the coffee"""

    def __init__(self):
        # Instance attribute — each CoffeeMaker object gets its own
        # copy of this dict. Stores current ingredient levels.
        # Note: "money" is not here — MoneyMachine owns that.
        # Separation of concerns: each class tracks only what it owns.
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        # Directly reads from self.resources and formats with units.
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        # `drink` here is a MenuItem object passed in from main.py.
        # drink.ingredients is the dict on that MenuItem: {"water": 200, "milk": 150, ...}
        # We compare each required amount against what's in self.resources.
        #
        # Design choice vs Day 15 version:
        #   Day 15 returned False immediately on the first failure.
        #   This version checks ALL ingredients before returning,
        #   so the user sees every shortage at once (better UX).
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False        # flag failure but keep looping
        return can_make                 # True only if no shortage was found

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        # `order` is a MenuItem object. order.ingredients gives the dict
        # of what this drink needs. We loop and subtract from self.resources.
        # Works because both dicts share the same keys (water, milk, coffee).
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        # order.name reads the name attribute directly off the MenuItem object.
        print(f"Here is your {order.name} ☕️. Enjoy!")