import tkinter as tk
from tkinter import ttk


#setup

window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')

#button
def button_func():
    print('a basic button')
    
button_string = tk.StringVar(value='A button with string var')

btn = ttk.Button(window, text='A simple button', command=lambda:print('a basic button'), textvariable=button_string)
btn.pack()

#checkbutton
check_var = tk.StringVar()
check = ttk.Checkbutton(   
    window,
    text='checkbox 1',
    command=lambda: print(check_var.get()),
    variable=check_var) # we don't use text variable because the var is not storing text but whether if the checkbox is checked
check.pack()

#1:11:35

#run
window.mainloop()