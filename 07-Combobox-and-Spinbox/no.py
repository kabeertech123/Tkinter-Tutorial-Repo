import tkinter as tk
from tkinter import ttk

# setup

window = tk.Tk()
window.geometry('600x400')
window.title('Combo & Spin')

# combobox
items = ('Ice cream', 'Pizza', 'Lamb')
food_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(window, textvariable= food_string)
combo['values'] = items
combo.pack()




window.mainloop()