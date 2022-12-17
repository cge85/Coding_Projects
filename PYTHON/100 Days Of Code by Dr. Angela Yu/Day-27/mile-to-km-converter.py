from tkinter import *


window = Tk()
window.title("Mile to Kilometers Converter")
window.config(padx=20,pady=20)

my_label = Label(text="is equal to", font=("Arial", 20))
my_label.grid(column=0, row=1)

convert_label = Label(text=0, font=("Arial", 20))
convert_label.grid(column=1, row=1)

miles_label = Label(text="Miles", font=("Arial", 20))
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=("Arial", 20))
km_label.grid(column=2, row=1)

my_input = Entry(width=10 ,font=("Arial", 20))
my_input.grid(column=1, row=0)

def miles_to_km():
    miles = float(my_input.get())
    km = round(1.609 * miles, 1)
    convert_label.config(text=km)
    
button = Button(text="Calculate",font=("Arial", 16), command=miles_to_km)
button.grid(column=1, row=2, ipadx=20, ipady=5)





window.mainloop()