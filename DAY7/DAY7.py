import random
import requests

# words = ['apple', 'mango', 'banana']

# chosen_word = random.choice(words)

# for letter in chosen_word:
#     blank_word += '_'
alphabets = "abcdefghijklmnopqrstuvwxyz"

def hangman():
    response = requests.get(f"https://api.datamuse.com/words?ml={random.choice(alphabets)}&max=1")
    print(response.status_code)
    # print(response.json())
    word_json = response.json()
    chosen_word = word_json[0]['word'].lower()
    word = list('_' * len(chosen_word))
    life = len(word)
    game_on = True
    print("Welcome to Hangman")
    print(' '.join(word))
    guessed_letters = []
    while game_on:
        guess_letter = input("Guess a letter: ").lower()
        if guess_letter.isalpha() and len(guess_letter) == 1:
            if guess_letter not in guessed_letters:
                if guess_letter in chosen_word:
                    print("Correct Guess!")
                    for i,letter in enumerate(chosen_word):
                        if guess_letter == letter:
                            word[i] = guess_letter
                        if letter == '-':
                            word[i] = '-'
                    if '_' not in word:
                        print(f"The word was {chosen_word}")
                        print("WINNER!!!!!!!")
                        break
                else:
                    life -= 1
                    print("Wrong guess")
                    if life == 0:
                        print("LOSER!!!!!!!!")
                        print(f"The correct word was {chosen_word}")
                        break
                print(f"You have {life} guesses left")
                print(' '.join(word))
                guessed_letters.append(guess_letter)
            else:
                print("You've already guessed this letter.")
        else:
            print("Enter Alphabet only.")

hangman()