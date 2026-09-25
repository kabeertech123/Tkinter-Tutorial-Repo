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

window.title('grid')

#widgets
lbl1 = tk.Label(window, text = 'lbl1', bg='red')
lbl2 = tk.Label(window, text = 'lbl2', bg='blue')
lbl3 = tk.Label(window, text = 'lbl3', bg='green')
lbl4 = tk.Label(window, text = 'lbl4', bg='violet')
btn1 = tk.Button(window, text = 'btn1')
btn2 = tk.Button(window, text = 'btn2')
entry = ttk.Entry(window)

# grid

window.columnconfigure(0, weight= 1)
window.columnconfigure(1, weight= 1)
window.rowconfigure(0, weight= 1)
window.rowconfigure(1, weight= 1)

# grid layout

lbl1.grid(row=0, column=0, sticky='nwes')
lbl2.grid(row=1, column=0, sticky='nsew')
lbl3.grid(row=0, column=1, sticky='nsew')
lbl4.grid(row=1, column=1, sticky='nsew')



window.mainloop()