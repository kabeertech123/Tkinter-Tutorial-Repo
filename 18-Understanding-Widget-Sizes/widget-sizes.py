import tkinter as tk
from tkinter import ttk

# setup

window = tk.Tk()
# centre the window

middle_width = window.winfo_screenwidth() 
middle_height = window.winfo_screenheight() 
window_width = 900
window_height = 600

left = int(middle_width / 2 - window_width / 2)
top = int(middle_height / 2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{left}+{top}')

window.title('widget sizes ')


#widgets
lbl1 = tk.Label(window, text = 'label 1', background='blue') 
lbl2 = tk.Label(window, text = 'label 2', background='red', width= 50)

# layout

lbl1.pack()
lbl2.pack(fill='x')



window.mainloop()

# Notes

'''
ttk.label(window, text = 'label', width = 50).pack(fill='x') 

tkinter will always take the pack to find the width rather than setting the width as 50 characters 

'''
