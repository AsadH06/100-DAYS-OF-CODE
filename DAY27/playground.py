
# ============================================================
# *args — variable positional arguments
# ============================================================

# *args collects any number of positional arguments into a TUPLE
def add(*args):
    sum_of_all_n = sum([n for n in args])  # args is a tuple: (1, 2, 3, 4, 5)
    print(sum_of_all_n)                    # list comprehension unpacks it, sum() adds them up

add(1, 2, 3, 4, 5)  # all 5 values go into args as a tuple


# ============================================================
# **kwargs — variable keyword arguments
# ============================================================

# **kwargs collects any number of keyword arguments into a DICT
def calculate(**kwargs):
    print(kwargs)        # {'add': 3, 'multiply': 5}
    print(type(kwargs))  # <class 'dict'>
    for key, value in kwargs.items():  # iterate like a normal dict
        print(key, value)
    print(kwargs["add"])  # access specific value by key

calculate(add=3, multiply=5)


# ============================================================
# **kwargs in a Class
# ============================================================

class Car:

    def __init__(self, **kw):  # **kw collects all keyword args passed to Car() into a dict
        self.make = kw["make"]        # direct key access — throws KeyError if key missing
        self.model = kw.get("model")  # .get() returns None if key missing instead of crashing
        self.color = kw.get("color")  # safe to use when argument is optional
        self.seats = kw.get("seats")

# if model wasn't passed: kw["model"] → KeyError, kw.get("model") → None
my_car = Car(make="Nissan", model="GTR")
print(my_car.make, my_car.model)


# ============================================================
# Combining a, *args, **kwargs together
# ============================================================

# rule: regular args first, then *args, then **kwargs
def all_aboard(a, *args, **kw):
    print(a, args, kw)
    # a    = 4           (first positional arg, goes to 'a')
    # args = (7, 3, 0)   (remaining positional args collected into tuple)
    # kw   = {'x': 10, 'y': 64}  (keyword args collected into dict)

all_aboard(4, 7, 3, 0, x=10, y=64)