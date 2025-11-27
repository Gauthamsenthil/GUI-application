from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("tk")
window.geometry('100x100')
def virus():
    messagebox.showwarning("Alert","Virus detected!")
button = Button(text = "scan for virus",fg = "black",bg = "lightgrey",command = virus)
button.pack()
window.mainloop()