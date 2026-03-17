bill = 0
print("Welcome to python pizza deliveries")

#TODO: Work out how much they need to pay based on their size choice.

def check_size(size,bill):
    if size == 's':
        bill += 15
    elif size == 'm':
        bill += 20
    elif size == 'l':
        bill += 25
    return bill

#TODO: Work out how much to add to their bill based on their pepperoni choice.

def add_pepperoni(size, bill):
    if size == 's':
        bill += 2
    elif size == 'm' or size == 'l':
        bill += 3
    return bill
#TODO: Work out their final amount based on whether if they want extra cheese.
def add_cheese(bill):
    return bill + 1

size = input("What size pizza do you want? S, M or L: ").lower()

bill = check_size(size, bill)

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()

if pepperoni == 'y':
    bill = add_pepperoni(size, bill)

extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

if extra_cheese == 'y':
    bill = add_cheese(bill)

print(f"Your final bill is ${bill}")



