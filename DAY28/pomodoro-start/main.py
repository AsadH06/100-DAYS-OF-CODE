from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check_mark = "✔"
reps = 0
counter = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global counter,reps
    window.after_cancel(timer)
    label_timer.config(text="Timer", fg=GREEN)
    label_checkmark.config(text="")
    reps,counter = 0,0
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, counter
    reps +=1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    if reps % 8 == 0:
        label_timer.config(text="BREAK", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        counter += 1
        label_checkmark.config(text=check_mark*counter)
        label_timer.config(text="BREAK", fg=PINK)
        count_down(short_break_sec)
    else:
        label_timer.config(text="WORK", fg=GREEN)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = count // 60
    count_sec = count % 60
    count_sec = f"0{count_sec}" if count_sec < 10 else count_sec
    count_min = f"0{count_min}" if count_min < 10 else count_min
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(50, count_down, count-1)
    else:
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


label_timer = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
label_timer.grid(row=0, column=1)

button_start = Button(text="Start", command=start_timer, font=(FONT_NAME,12,"bold"), highlightthickness=0)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", command=reset_timer, font=(FONT_NAME,12,"bold"), highlightthickness=0)
button_reset.grid(row=2, column=2)

label_checkmark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "bold"))
label_checkmark.grid(row=3, column=1)










window.mainloop()

