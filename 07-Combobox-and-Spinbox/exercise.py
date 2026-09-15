import tkinter as tk
from tkinter import ttk

# setup

window = tk.Tk()
window.geometry('600x400')
window.title('Exercise')


# widget
arr = ['A' ,'B', 'C', 'D', 'E']
spin_string = tk.StringVar(value=arr[0])
spin = ttk.Spinbox(window, textvariable=spin_string)
spin['values'] = arr
spin.pack()

# events

spin.bind('<<Decrement>>', lambda event : print(spin_string.get()))


window.mainloop()