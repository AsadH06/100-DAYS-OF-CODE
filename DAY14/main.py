from art import logo, vs
from game_data import data
import random
import os

def compare(acc1, acc2):
    if acc1['follower_count'] > acc2['follower_count']:
        return acc1
    else:
        return acc2

def format_data(acc):
    acc_name = acc['name']
    acc_desc = acc['description']
    acc_country = acc['country']
    return f"{acc_name}, a {acc_desc}, from {acc_country}"



a = random.choice(data)
game_is_on = True
score = 0
print(logo)

while game_is_on:
    b = random.choice(data)
    if a ==b:
        b = random.choice(data)

    # print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(f"Compare A: {format_data(a)}")
    print(vs)
    # print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
    print(f"Compare B: {format_data(b)}")

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_guess == 'a':
        user_guess = a
    else:
        user_guess = b

    answer = compare(a, b)

    if user_guess['name'] == answer['name']:
        score +=1
        os.system('cls')
        print(logo)
        print(f"You're right! Current score: {score}.")
        a = answer
    else:
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_is_on = False





