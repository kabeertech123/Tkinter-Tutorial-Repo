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
check_var = tk.BooleanVar()
check = ttk.Checkbutton(   
    window,
    text='checkbox 1',
    command=lambda: print(check_var.get()),
    variable=check_var,# we don't use text variable because the var is not storing text but whether if the checkbox is checked
    #onvalue = 10,offvalue= 5  # WHen check_var is an int, it sets the value of 10 when its checked and 5 when unchecked
     ) 
check.pack()

# radio buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(window,
    text = 'RadioButton 1',
    variable=radio_var, # You have to set a custom value for each radio button otherwise they will all be the same = 0 
    value = 'radio 1',
    command= lambda: print(radio_var.get())
    )
radio1.pack()
# Both
radio2 = ttk.Radiobutton(
    window,
    text = 'RadioButton 2',
    value = 2,
    variable=radio_var,
    command= lambda: print(radio_var.get())
    )
radio2.pack()

#1:11:35

#run
window.mainloop()