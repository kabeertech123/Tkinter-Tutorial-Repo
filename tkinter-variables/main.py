import tkinter as tk
from tkinter import ttk

def button_func():
    # get the content of the entry
    print(entry.get())

# window

window = tk.Tk()
window.title('Getting and Setting widgets')
# 👇 This makes the window always on top (until you remove it)
window.attributes('-topmost', 1)


#widgets

label = ttk.Label(master=window, text='this is a label', font='Calibri 25 bold')
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text='Click me for free money', command=button_func)
button.pack()


#run 
window.mainloop()


