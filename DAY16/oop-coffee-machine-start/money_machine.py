# ─────────────────────────────────────────────────────────────
#  money_machine.py — MoneyMachine class
#
#  Handles everything money-related: collecting coins, calculating
#  totals, giving change, and tracking profit.
#
#  OOP concepts used here:
#    Class attributes  — CURRENCY and COIN_VALUES are shared across
#                        all MoneyMachine instances (defined on the class,
#                        not on self). Since these never change per-instance,
#                        putting them on the class saves memory and signals
#                        that they're constants.
#    Instance attributes — self.profit and self.money_received are unique
#                          to each instance and change over time.
# ─────────────────────────────────────────────────────────────
class MoneyMachine:

    # ── Class attributes ──────────────────────────────────────
    # Defined directly on the class, not inside __init__.
    # Accessed as self.CURRENCY or MoneyMachine.CURRENCY — both work.
    # Changing CURRENCY here updates it for every instance at once.
    CURRENCY = "$"

    # COIN_VALUES maps coin names (used as input prompts) to their dollar values.
    # Using a dict means adding a new coin type is one line here — nothing else changes.
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        # ── Instance attributes ────────────────────────────────
        # self.profit      — total money earned across all transactions
        # self.money_received — amount inserted in the *current* transaction only,
        #                       reset to 0 after every transaction (see make_payment)
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        # Uses the class attribute CURRENCY for the symbol.
        # f-string formats it as e.g. "Money: $7.5"
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        # Loops through COIN_VALUES dict — each key is the coin name (used in the prompt),
        # each value is the dollar amount per coin.
        # int(input(...)) gets the coin count, multiply by coin value, add to running total.
        # self.money_received accumulates across the loop so we get one total at the end.
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        # Calls process_coins() first to collect and total the inserted coins.
        # Note: process_coins() modifies self.money_received as a side effect,
        # so after this call self.money_received holds the full amount inserted.
        self.process_coins()

        if self.money_received >= cost:
            # round(..., 2) prevents floating-point errors like $0.30000000000000004
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")

            # Only add the drink's cost to profit — not the full amount inserted.
            # Change given back is never counted as revenue.
            self.profit += cost

            # Reset for the next transaction — instance state stays clean.
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            # Reset so leftover amount from a failed transaction doesn't
            # carry over and affect the next customer's payment.
            self.money_received = 0
            return False