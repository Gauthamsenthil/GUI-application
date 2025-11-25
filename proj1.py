from tkinter import *

root = Tk()
root.title('Multiply')
root.geometry('300x300')

# Label and Entry for first number
label1 = Label(root, text='Enter your first number', bg='lightblue', fg='black')
label1.pack()
entry_n1 = Entry(root)
entry_n1.pack()

# Label and Entry for second number
label2 = Label(root, text='Enter your second number', bg='lightblue', fg='black')
label2.pack()
entry_n2 = Entry(root)
entry_n2.pack()

# Function to multiply
def multiply():
    n1 = int(entry_n1.get())
    n2 = int(entry_n2.get())
    result = n1 * n2
    result_label = Label(root, text='The result is ' + str(result), bg='lightgreen', fg='black')
    result_label.pack()

# Button
btn = Button(root, text='Multiply', command=multiply, bg='orange', fg='black')
btn.pack()

root.mainloop()
