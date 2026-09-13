import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')

def radio_func():
    print(check_bool.get())
    check_bool.set(False)

# data 
radio_var = tk.StringVar()
check_bool = tk.BooleanVar()

# widgets

radio1 = ttk.Radiobutton(
    window,
    text = 'radio A',
    variable=radio_var,
    value='A',
    command= radio_func
)

radio2 = ttk.Radiobutton(
    window,
    text = 'radio B',
    variable=radio_var,
    value='B',
    command = radio_func
)



check = ttk.Checkbutton(
    window,
    text='Click to print Radio button values',
    variable=check_bool,
    command= lambda : print(radio_var.get())
   
    
)


# Layout
radio1.pack()
radio2.pack()
check.pack()

window.mainloop()