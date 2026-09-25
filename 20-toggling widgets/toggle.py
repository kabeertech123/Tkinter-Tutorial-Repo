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

window.title('hide widgets')

# place

def toggle_label_place():
    lbl.place_forget()
    
btn = tk.Button(window, text= 'toggle label', command=toggle_label_place)
btn.place(x=10, y = 10)

lbl = tk.Label(window, text='A label')
lbl.place(relx = 0.5, rely=0.5, anchor='center')


window.mainloop()