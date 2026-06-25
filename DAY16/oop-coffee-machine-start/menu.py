# ─────────────────────────────────────────────────────────────
#  menu.py — Contains two classes: MenuItem and Menu
#
#  MenuItem models a single drink (its name, ingredients, cost).
#  Menu models the full list of available drinks and provides
#  methods to interact with that list.
#
#  These two classes have a "composition" relationship:
#  Menu *contains* a list of MenuItem objects — each drink on
#  the menu is a fully-formed object, not just raw data.
# ─────────────────────────────────────────────────────────────


# ─────────────────────────────────────────────────────────────
#  class MenuItem
#
#  A blueprint for a single drink on the menu.
#  Each MenuItem instance stores everything about one drink:
#  its name, cost, and ingredient amounts.
#
#  OOP concept — Encapsulation:
#  All data about a drink is bundled into one object.
#  Instead of a loose dict like {"name": "latte", "cost": 2.5},
#  we get an object with structured attributes we can access
#  cleanly: item.name, item.cost, item.ingredients
# ─────────────────────────────────────────────────────────────
class MenuItem:
    """Models each Menu Item."""

    # __init__ is the constructor — called automatically when you do MenuItem(...)
    # `self` refers to the specific instance being created.
    # Each parameter becomes an attribute stored on that instance.
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        # Ingredients are stored as a dict so CoffeeMaker can loop through
        # them by key and match them directly to its own resources dict.
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


# ─────────────────────────────────────────────────────────────
#  class Menu
#
#  A blueprint for the full menu — holds a list of MenuItem
#  objects and provides methods to work with them.
#
#  OOP concept — Composition:
#  Menu doesn't inherit from MenuItem; it *contains* MenuItem
#  objects inside a list. "Has-a" relationship: a Menu has items.
# ─────────────────────────────────────────────────────────────
class Menu:
    """Models the Menu with drinks."""

    def __init__(self):
        # self.menu is a list of MenuItem instances.
        # Each drink is a proper object — not a raw dict or string.
        # To add a new drink, just add another MenuItem(...) here.
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        # Builds a string like "latte/espresso/cappuccino/" for the input prompt.
        # Loops through self.menu and reads item.name from each MenuItem object.
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name.
        Returns that item if it exists, otherwise returns None."""
        # Loops through MenuItem objects and checks their .name attribute.
        # Returns the full MenuItem object (not just its name) so the caller
        # gets access to .cost and .ingredients too.
        for item in self.menu:
            if item.name == order_name:
                return item         # returns the MenuItem object itself

        # If no match was found after the full loop, print an error and
        # return None. The caller (main.py) checks for None and skips brewing.
        print("Sorry that item is not available.")
        # Python returns None implicitly here, but the docstring makes it explicit.