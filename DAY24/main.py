# file = open('my_file.txt')

"""READING THE FILE"""

""" C:/Users/Asadm/OneDrive/Desktop/my_file.txt       -> absolute path """
""" ../../my_file.txt     -> moving up two levels """
with open("../../my_file.txt") as file:
    contents = file.read()
    print(contents)


""" WRITING THE FILE"""
# w -> write
# a -> add
# if you open the file in w mode and file doesn't exist, then the file will be created with the content inside it.
with open("../../my_file.txt", mode="a") as file:
    file.write("\nNew text.")
