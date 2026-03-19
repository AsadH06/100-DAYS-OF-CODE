import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','*','(',')' ]


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input("How many symbols would you like? \n"))
nr_numbers = int(input("How many numbers would you like? \n"))

password = []
for letter in range(nr_letters):
    l = random.choice(letters)
    password.append(l)

for symbol in range(nr_symbols):
    s = random.choice(symbols)
    password.append(s)

for number in range(nr_numbers):
    n = random.choice(numbers)
    password.append(n)

### SHUFFLING USING .SAMPLE() -> STORED IN NEW VARIABLE
password_new = random.sample(password, len(password))
print(''.join(password_new))

### BEFORE SHUFFLE
print("Original password generation: "+''.join(password))
random.shuffle(password)
### AFTER SHUFFLE
print(''.join(password))
