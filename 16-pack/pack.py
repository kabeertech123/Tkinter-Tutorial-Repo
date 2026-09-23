#notes 

'''
side determines the direction of the widgets

expand:True,False – determines how much space a widget can occupy, ONLY IN 1 DIRECTION

'''


import tkinter as tk
from tkinter import ttk

# setup

window = tk.Tk()
# centre the window

middle_width = window.winfo_screenwidth() 
middle_height = window.winfo_screenheight() 
window_width = 400
window_height = 600

left = int(middle_width / 2 - window_width / 2)
top = int(middle_height / 2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{left}+{top}')

window.title('pack')

# widgets
label1 = tk.Label(window, text = 'First label', background='red')
label2 = tk.Label(window, text = '2nd label', background='blue')
label3 = tk.Label(window, text = 'last of the labels', background='green')
button = tk.Button(window, text = 'button')

#layout
label1.pack(side='top', fill='both', pady=10, padx= 10, ipady=100)
label2.pack(side='left', expand=True, fill='both')
label3.pack(side='top', fill='both', expand=True)
button.pack(side='top', fill='both', expand=True)



window.mainloop()

