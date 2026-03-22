import math

def life_in_weeks(age):
    total_weeks = 90 * 52
    age_in_weeks = age * 52
    weeks_left = total_weeks - age_in_weeks
    return weeks_left

# age = int(input("Enter your age: "))
# age_weeks_left = life_in_weeks(age)
# print(f"You have {age_weeks_left} weeks left.")

def calculate_love_score(name1, name2):
    true = ['t', 'r', 'u', 'e']
    love = ['l', 'o', 'v', 'e']
    count_true = 0
    count_love = 0
    for letter in true:
        l1 = name1.lower().count(letter)
        l2 = name2.lower().count(letter)
        count_true += l1 + l2
    for letter in love:
        l1 = name1.lower().count(letter)
        l2 = name2.lower().count(letter)
        count_love += l1 + l2
    love_sum = f"{count_true}{count_love}"
    print(love_sum)
calculate_love_score('Kanye West', 'Kim Kardashian')