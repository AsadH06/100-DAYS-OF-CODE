from tkinter import *

window = Tk()
window.title("grid")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

label = Label(text="This is old text")
label.grid(row=0, column=0)

def action():
    print("Yo")
button1 = Button(text="Click me", command=action)
button1.grid(row=1, column=1)

def play():
    print("Play")

button2 = Button(text="New Button", command=action)
button2.grid(row=0, column=2)

entry = Entry(width=30)
entry.insert(END, string="some text")
print(entry.get())
entry.grid(row=2, column=3)




window.mainloop()