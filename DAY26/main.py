from typing import List

numbers = [1,2,3]

new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

print(new_list)
# LIST COMPREHENSION
new_list_comprehension = [n+1 for n in numbers]
print(new_list_comprehension)

name = "Asad"
new_name = [letter for letter in name]
print(new_name)

double = [item*2 for item in range(1,5)]
print(double)

names = ["alex","Beth","Caroline","Dave","Eleanor","Freddie"]
short_names = [name for name in names if len(name) < 5]
caps_names = [name.upper() for name in names if len(name) >= 5]
print(short_names, caps_names)

"""Filtering Even Numbers
In this list comprehension exercise you will practice using list comprehension to filter out the even numbers from a series of numbers.   
First, use list comprehension to convert the list_of_strings to a list of integers called numbers.   
Then use list comprehension again to create a new list called result.
This new list should only contain the even numbers from the list numbers. 
Again, try to use Python's List Comprehension instead of a Loop. 
"""

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num%2 == 0]
print(result)

"""Data Overlap
💪 This exercise is HARD 💪 
Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. 
You are going to create a list called result which contains the numbers that are common in both files. 
e.g. if file1.txt contained: 
1 
2 
3
and file2.txt contained: 
2
3
4
result = [2, 3]
IMPORTANT:  The output should be a list of integers and not strings!
Try to use List Comprehension instead of a Loop. 
"""
with open('file1.txt') as file1:
    num1 = file1.readlines()
    print(num1)
    stripped_num1 = [int(num.strip()) for num in num1]

with open('file2.txt') as file2:
    num2 = file2.readlines()
    stripped_num2 = [int(num.strip()) for num in num2]

result = [num for num in stripped_num1 if num in stripped_num2]

print(result)


""" DICTIONARY COMPREHENSION """
""" new_dict = {new_key:new_value for item in list if test} """
""" new_dict = {new_key:new_value for (key,value) in dict.items()) if test} """

import random
names = ["alex","Beth","Caroline","Dave","Eleanor","Freddie"]
student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)
passed_students = {name:score for (name,score) in student_scores.items() if score >= 60 }
print(passed_students)

"""Dictionary Comprehension 1
You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.   
Try Googling to find out how to convert a sentence into a list of words.  *
*Do NOT** Create a dictionary directly.
Try to use Dictionary Comprehension instead of a Loop. 
To keep this exercise simple, count any punctuation following a word with no whitespace as part of the word. Note that "Swallow?" therefore has a length of 8."""

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word:len(word) for word in sentence.split()}
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:((temp * 9/5) + 32) for day,temp in weather_c.items()}
print(weather_f)


"""COMPREHENSION USING PANDAS"""

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}

import pandas as pd

# pd.DataFrame(dict) — converts a dictionary into a DataFrame
# keys become column names, values (lists) become column data
student_df = pd.DataFrame(student_dict)
print(student_df)
# output:
#   student  score
# 0  Angela     56
# 1   James     76
# 2    Lily     98

# .items() — iterates over columns, not rows
# each iteration gives: (column_name, Series of that column's values)
# same as dict.items() but for DataFrames
for key, value in student_df.items():
    print(key)    # prints column name: "student", then "score"
    print(value)  # prints the full Series for that column including index labels

# .iterrows() — iterates over rows
# each iteration gives: (index_label, Series of that row's values)
# the Series contains all column values for that row, accessible by column name
for (index, row) in student_df.iterrows():
    # print(index)     # prints row number: 0, 1, 2
    # print(row)       # prints entire row as a Series with column names as index
    # print(row.student) # dot notation to access specific column value in that row
    print(row.score)   # prints score for each row: 56, 76, 98