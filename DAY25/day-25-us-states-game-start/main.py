import turtle
import pandas as pd
from mapping import Mapping

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)       # must register gif as a shape before using it
turtle.shape(image)          # set the screen background as the map image

# message turtle — persistent object outside function so we're not
# creating a new Turtle object every time the user guesses wrong
message_turtle = turtle.Turtle()
message_turtle.hideturtle()
message_turtle.penup()

def guessed():
    message_turtle.clear()   # clear previous message before writing new one
    message_turtle.goto(0, 0)
    message_turtle.write(arg="ALREADY GUESSED\nTry Again...", align="center", font=('Courier', 24, 'normal'))
    # NOTE: textinput() is blocking — it freezes the program until user responds
    # so this message naturally stays visible until next input is submitted

mapping = Mapping()          # turtle that writes state names on the map
states_guessed = []
data = pd.read_csv("50_states.csv")        # load all 50 states with x, y coordinates
data_states = data['state'].to_list()      # plain Python list of all state names for comparison later

while True:
    states_guessed_len = len(states_guessed)  # recalculated every tick so title updates correctly
    answer_state = screen.textinput(
        title=f"{states_guessed_len}/50 States correct",
        prompt="What's another state name?"
    )
    message_turtle.clear()
    # textinput() returns None when user clicks Cancel — must check before calling .title()
    # calling .title() on None causes AttributeError: 'NoneType' has no attribute 'title'
    if answer_state is None:
        break

    answer_state = answer_state.title()  # normalize input to Title Case to match CSV format

    if answer_state == "Exit":           # allow user to quit gracefully by typing "Exit"
        missing_state = [state for state in data_states if state not in states_guessed]
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("states_to_learn_1.csv")
        break

    # filter the DataFrame to find the matching state row
    # returns empty DataFrame if no match — .empty property (not method, no brackets) checks this
    answer_df = data[data['state'] == answer_state]

    if answer_df.empty:
        continue                         # wrong guess, just loop again silently
    else:
        # iloc[0] gets first row by POSITION — safe after filtering because
        # pandas preserves original index labels, so ['x'][0] would KeyError
        # if the state wasn't at row 0 in the original DataFrame
        state = answer_df.iloc[0]['state']
        x_cor = answer_df.iloc[0]['x']
        y_cor = answer_df.iloc[0]['y']

        if answer_state in states_guessed:
            guessed()                    # show already guessed message
        else:
            states_guessed.append(answer_state)
            mapping.write_on_map(x_cor, y_cor, answer_state)  # place state name on map
            if states_guessed_len >= 50:
                break                    # all 50 states guessed, end game


# save states the user didn't guess so they can study them
# set difference: all states minus guessed states = missing states
states_not_guessed = list(set(data_states) - set(states_guessed))
sng_data = pd.Series(states_not_guessed)
sng_data.to_csv("states_to_learn.csv")  # saves with index by default — use index=False to remove it

# ============================================================
# LEARNINGS AND NOTES
# ============================================================

# PANDAS CORE CONCEPTS:
# pd.read_csv()        — loads CSV into a DataFrame (table structure)
# df['col']            — selects a column, returns a Series
# df[df.col == value]  — filters rows, returns new DataFrame with original index labels preserved
# .empty               — property (no brackets), True if DataFrame has no rows
# .iloc[0]             — gets first row by POSITION, safe after filtering
# ['col']              — gets column value from a row
# .to_list()           — converts Series to plain Python list
# pd.Series(list)      — creates a Series from a Python list
# .to_csv()            — saves Series/DataFrame to CSV file

# KEY BUGS ENCOUNTERED:
# 1. textinput() returns None on cancel — always check before calling string methods on it
# 2. .empty() with brackets crashes — it's a property, not a method
# 3. filtered['x'][0] KeyError — pandas keeps original index labels after filtering,
#    use iloc[0] to access by position instead
# 4. creating Turtle() inside a function every call — accumulates objects in memory,
#    better to keep a persistent turtle outside and reuse it
# 5. "".join(states) smashes names together — use "\n".join() or pandas to_csv() for proper formatting