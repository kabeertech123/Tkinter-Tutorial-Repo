import tkinter as tk
from tkinter import ttk

# create a window
window = tk.Tk()
window.title('Window and Widets')
window.geometry('800x500')


# 👇 This makes the window always on top (until you remove it)
window.attributes('-topmost', 1)

# ttk widgets
label = ttk.Label(master=window, text='This is a test') # label is below pack so therefore, its will be placed at the bottom
label.pack()


# create.widgets
text = tk.Text(master=window)
text.pack()#places it in the middle top of the window


# run 
window.mainloop() # updates GUI and checks for events 