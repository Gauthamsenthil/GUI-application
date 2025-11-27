from tkinter import *

window = Tk()
window.title("Length Converter App")
window.geometry('400x400')

label1 = Label(text="give the length (in inches)")
label1_entry = Entry(window)
label1.pack()
label1_entry.pack()

label3 = Label(text="")
label3.pack()

def convert(event=None):
    inches = float(label1_entry.get())
    centimeters = inches * 2.54
    label3.config(text="Inches to cm: " + str(centimeters) + " cm")


window.bind("<Return>", convert)

button = Button(text="Convert", command=convert)
button.pack()

window.mainloop()
