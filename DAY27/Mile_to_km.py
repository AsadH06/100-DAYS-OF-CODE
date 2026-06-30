from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

label1 = Label(text="is equal to")
label1.grid(row=1, column=0)



label2 = Label(text="Miles")
label2.grid(row=0, column=2)

label4 = Label(text="0")
label4.grid(row=1, column=1)

label3 = Label(text="Km")
label3.grid(row=1, column=2)

def calculate():
    miles = int(entry.get())
    km = round(miles * 1.60934, 2)
    label4.config(text=f"{km}")

button1 = Button(text="Calculate", command=calculate)
button1.grid(row=2, column=1)

entry = Entry(width=7)
entry.insert(END, string="0")
entry.grid(row=0, column=1)

window.mainloop()
