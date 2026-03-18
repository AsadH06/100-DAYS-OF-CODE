### RANDOMIZATION
import random

"""
random.randint(1, 10)
random.random() -> between 0 and 1
random.uniform(1,10) 
random.choice()
"""


### LISTS
""" 
states = []
states.append(x)
states.extend()
states.insert(i, x)
state.remove(x)
state.pop()
"""

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

length_list = len(friends)
bill_paid_by = random.randint(0, length_list-1)
# print(friends[bill_paid_by])

print(random.choice(friends))
