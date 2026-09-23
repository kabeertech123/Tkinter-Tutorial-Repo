import tkinter as tk
from tkinter import ttk
import math

# setup




window = tk.Tk()

middle_width = window.winfo_screenwidth() 
middle_height = window.winfo_screenheight() 
window_width = 1400
window_height = 600

left = int(middle_width / 2 - window_width / 2)
top = int(middle_height / 2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{left}+{top}')

window.title('middle')


window.mainloop()


#set the window to be in the middle