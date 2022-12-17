from tkinter import *

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24))
my_label.grid(column=0, row=0)
my_label.config(padx=100, pady=100)

# my_label["text"] = "new text"
# my_label.config(text= "Testing changing text")


#Button
def button_clicked():
    my_label.config(text=input.get())

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

def button_clicked2():
    my_label.config(text=input.get())

new_button = Button(text="New Button", command=button_clicked2)
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
input.grid(column=3, row=2)
print(input.get())










window.mainloop()
