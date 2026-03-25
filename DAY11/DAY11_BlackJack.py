import random
from art import logo


def draw_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    sum_card = sum(cards)
    if sum_card == 21 and len(cards) == 2:
        return 0
    if sum_card > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    # while sum_card > 21 and 11 in cards:
    #     cards.remove(11)
    #     cards.append(1)
    return sum_card


bj = False


def compare(user_s, comp_s):
    if comp_s == user_s:
        return "It's a draw"
    elif comp_s == 0:
        return "Computer has BLackJack, bad luck :("
    elif user_s == 0:
        return "You won by BlackJack!"
    elif user_s > 21:
        return "You went over, You lose :( "
    elif comp_s > 21:
        return "Opponent went over, You win!!!"
    elif comp_s < user_s:
        return "You win :))))"
    else:
        return "You lose :("


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1

    for i in range(2):
        user_cards.append(draw_cards())
        computer_cards.append(draw_cards())

    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            continue_drawing = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if continue_drawing == 'y':
                user_cards.append(draw_cards())
            else:
                is_game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(draw_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()

