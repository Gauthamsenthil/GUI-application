#import necessary libraries
from tkinter import *
from datetime import date
#create window
root = Tk()
root.title("getting started with widgets")
root.geometry('400x300')
#add widgets
#add labels
lb1 = Label(text = "hey there!",fg = "white",bg = "lightblue",height = 1,width = 300)
#add labe; for getting name as input from user
#use entry widget to create a text box for user to enter details
name_lb1 = Label(text = "full name", bbg = "white")
name_entry = Entry()

#function to display a message
def display():
    #read input given by user
    name = name_entry.get()
    message = "welcome to the application! \n today's date is:"
    greet = "hello "+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())

text_box = Text(height = 3)
btn = Button(text = "begin",command = display,height = 1,bg = "#1261A0",fg = "white")
#organise all the widgets in the window
lb1.pack
name_lb1.pack()
name_entry.pack()
btn.pack()
text_box.pack()

#run the application
root.mainloop()