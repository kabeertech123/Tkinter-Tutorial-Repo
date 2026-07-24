import tkinter as tk
from tkinter import ttk

# create a window
window = tk.Tk()
window.title('Window and Widets')
window.geometry('800x500')

#list of all the functions

def button_func():
    print('the btn was pressed')
    
def print_hello():
    print('hello')


# 👇 This makes the window always on top (until you remove it)

window.attributes('-topmost', 1)

# ttk widgets
label = ttk.Label(master=window, text='This is a test') # label is below pack so therefore, its will be placed at the bottom
label.pack()


# create.widgets
text = tk.Text(master=window)
text.pack()#places it in the middle top of the window

# ttk entry 

entry = ttk.Entry(master=window)
entry.pack()

new_text = ttk.Label(master=window, text='my label')
new_text.pack()

hello_button = ttk.Button(master=window, text="btn", command=print_hello)
hello_button.pack()

#ttk btn

#btn = ttk.Button (master=window, text='A button', command=button_func) 
btn = ttk.Button (master=window, text='A button', command=lambda : print('hello')) 
btn.pack()



#Exercise 
# add one more text label and a button with a function that prints 'hello'
#The label should say my label and be betwwen the entry widget an the button




# run 
window.mainloop() # updates GUI and checks for events 