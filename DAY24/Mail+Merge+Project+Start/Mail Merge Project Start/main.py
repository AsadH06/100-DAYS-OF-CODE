# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# open the template letter and read all lines into a list
with open("./Input/Letters/starting_letter.txt") as file:
    content = file.readlines()  # readlines() returns a list where each element is one line including \n
    print(type(content))
    print(content)
    # open the names file inside the same with block (both files stay open together)
    with open("./Input/Names/invited_names.txt") as file_names:
        names = file_names.readlines()  # same as above, each name is one element with \n at end
        print(names)
        print(type(names))
    for name in names:
        letter = "".join(content)   # join list of lines back into one single string
        name = name.strip("\n")     # remove newline character from end of each name
                                    # NOTE: strip() only removes from edges — works here because
                                    # \n is always at the very end of each name string
        # replace the placeholder [name] with the actual name
        # NOTE: replace() returns a NEW string, must assign back to a variable
        # your initial mistake was not saving the return value: letter.replace(...) does nothing alone
        letter_new = letter.replace("[name]", f"{name}")

        # create a new txt file for each person in the ReadyToSend folder
        # mode="w" creates the file if it doesn't exist, overwrites if it does
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter_file:
            letter_file.write(letter_new)  # write the personalized letter to the file