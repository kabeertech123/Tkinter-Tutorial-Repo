# sliders and a progress bar show progress in one direction
# sliders can be moved by the user or set independently
# progress bar can only be set independently


import tkinter as tk
import math
from tkinter import ttk

# setup

window = tk.Tk()
window.geometry('600x400')
window.title('Sliders')

# Widgets
scale_value = tk.IntVar()
scale = ttk.Scale(window, 
    command = lambda value : print(int(float(value))),
    from_ = 0, to = 10,
    length = 300,
    variable=scale_value
    )
scale.pack()

label = ttk.Label(window, textvariable=scale_value) 
label.pack()

# progress bar

progress = ttk.Progressbar(window, variable=scale_value, maximum= 10, mode = 'determinate')
progress.pack()

window.mainloop()