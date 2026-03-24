from sys import int_info
import os

calc_logo = r'''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
'''


def calculator():
    print(calc_logo)
    def add(n1, n2):
        return n1 + n2
    def subtract(n1, n2):
        return n1 - n2
    def multiply(n1, n2):
        return n1 * n2
    def divide(n1, n2):
        return n1 / n2

    calci = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }

    # calculating = True
    result = 0
    num1 = float(input("What's the first number: "))
    while True:
        for symbol in calci:
            print(symbol)
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number: "))


        result = float(round(calci[operation](num1,num2), 2))

        print(f"{num1} {operation} {num2} = {result}")
        cont_calci = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or type 'x' to exit.").lower()

        if cont_calci == 'y':
            num1 = result
            continue
        elif cont_calci == 'n':
            os.system('cls')
            calculator()
        else:
            os.system('cls')
            break

calculator()

"""
import operator

calci = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}
Python's built-in operator module has all the basic math operations as functions already — no need to define add, subtract etc. yourself!
"""