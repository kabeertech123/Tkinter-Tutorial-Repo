# sliders and a progress bar show progress in one direction
# sliders can be moved by the user or set independently
# progress bar can only be set independently


import tkinter as tk
from tkinter import ttk


# setup

window = tk.Tk()
window.geometry('600x400')
window.title('Sliders')

# Widgets
scale_value = tk.StringVar()
scale = ttk.Scale(window, command= 
    lambda value : print(value),
    from_ = 0, to = 10,
    length=300,
    variable=scale_value
    )
scale.pack()

label = ttk.Label(window, textvariable=scale_value) 
label.pack()


window.mainloop()