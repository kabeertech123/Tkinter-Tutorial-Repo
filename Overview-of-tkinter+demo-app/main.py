import tkinter as tk# gives us the basic logic
from tkinter import ttk #ttk contains all the widgets that we need

# There are 3 major components in tkinter 

"""
Widgets – GUI (Buttons, Text, Entry Field)

Layout – How the widgets are arranged on the window

Style – Determines font, color, size of widgets 

:)

"""

#convert functionality

def convert():
    print('convert')

# Window
window = tk.Tk()
window.title('demo')
window.geometry('400x300')

# 👇 This makes the window always on top (until you remove it)
window.attributes('-topmost', 1)

# title
title_label = ttk.Label(master=window, text='Miles to Kilometers', font='Calibri 25 bold')
title_label.pack()

#input field

input_frame = ttk.Frame(master=window)
entry = ttk.Entry(master=input_frame)
btn = ttk.Button(master=input_frame, text='Convert', command= convert)
entry.pack(side='left', padx=10)
btn.pack(side='left', padx= 10)
input_frame.pack(pady=10)

# output
output_label = ttk.Label(master=window, text='Output: ', font='Calibri 25 ')
output_label.pack(pady=5)


# Run 

window.mainloop()



