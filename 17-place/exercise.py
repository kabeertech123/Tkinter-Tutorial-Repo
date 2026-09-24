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

window.title('place exercise')

# widgets

lbl1 = tk.Label(window, text='Label', background='green')

# layout

lbl1.place(anchor='center', relx=0.5, rely=0.5, relwidth=0.5, relheight=0.3)



window.mainloop()