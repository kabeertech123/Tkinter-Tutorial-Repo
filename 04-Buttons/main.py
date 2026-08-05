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

#run
window.mainloop()