class User:

    """INITIALIZING: CONSTRUCTOR"""
    def __init__(self, user_id, username):
        print("New user created")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0


    def follow(self, user):
        user.followers += 1
        self.following += 1



        # initialize attributes

user1 = User(1, "asxpd")
user2 = User(2, "z1ya.s")

user2.follow(user1)

print(user1.followers, user1.following)
print(user2.followers, user2.following)







# user_1 = User("001", "angela")
# user_1.id = "001"
# user_1.username = "angela"

# user_2 = User("002", "asad")
# user_2.id = "001"
# user_2.username = "angela"

# print(user_1.id, user_2.id)
# print(user_1.username, user_2.username)
# print()