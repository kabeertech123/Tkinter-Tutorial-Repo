import tkinter as tk
from tkinter import ttk

# setup

window = tk.Tk()
window.geometry('600x400')
window.title('Combo & Spin')

# combobox
items = ('Ice cream', 'Pizza', 'Lamb')
food_string = tk.StringVar()
combo = ttk.Combobox(window, textvariable= food_string)
combo['values'] = items
combo.pack()

# events 
combo.bind('<<ComboboxSelected>>', lambda event : combo_label.config(text=f'Selected value: {food_string.get()}'))
# if you want to change the label when the combobox is selecteed then you have to use the combo.bind rather than using text in combo_label
  
combo_label = ttk.Label(window)
combo_label.pack()

# Spinbox

num_int = tk.IntVar(value = 12 )
spinbox = ttk.Spinbox(window, textvariable=num_int, from_ = 1, to = 20, increment = 2, ) #command=lambda : print('an arrow is pressed')
spinbox.bind('<<Increment>>', lambda event : print('up'))
spinbox.bind('<<Decrement>>', lambda event : print('down') )
spinbox.pack()




window.mainloop()