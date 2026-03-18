import random

rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
papers = '''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, papers, scissors]

def rps_input():
    user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: \n"))
    print(f'You chose: \n {game[user_choice]}')
    comp_choice = random.randint(0,2)
    print(f'Computer chose: \n {game[comp_choice]}')
    return user_choice, comp_choice

is_win = False
user_score = 0
comp_score = 0

while not is_win:
    user_choice, comp_choice = rps_input()
    if user_choice == comp_choice:
        print("It's a draw")

    # elif user_choice == 1 and comp_choice == 0 or user_choice == 0 and comp_choice == 2 or user_choice == 2 and comp_choice == 1:
    elif (user_choice - comp_choice) % 3 == 1:
        user_score +=1
        print("User wins")
        if user_score >=2:
            print("You win!")
            is_win = True
    elif user_choice == 0 and comp_choice == 1 or user_choice == 2 and comp_choice == 0 or user_choice == 1 and comp_choice == 2:
        comp_score += 1
        print("Computer wins")
        if comp_score >=2:
            is_win = True
            print("You lose")
    print(f"User score: {user_score} \nComp score: {comp_score}")

