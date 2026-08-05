import tkinter as tk # gives us the basic logic
# from tkinter import ttk  ttk contains all the widgets that we need
import ttkbootstrap as ttk #makes tkinter looks better 

# There are 3 major components in tkinter 

"""
Widgets – GUI (Buttons, Text, Entry Field)

Layout – How the widgets are arranged on the window

Style – Determines font, color, size of widgets 

:)

"""

#convert functionality

def convert():
    
    output_string.set(entry_int.get() * 1.61) # sets the output sting label the km value 

# Window
#window = tk.Tk()
window = ttk.Window(themename='darkly')
window.title('demo')
window.geometry('400x300')

# 👇 This makes the window always on top (until you remove it)
window.attributes('-topmost', 1)
        
# title
title_label = ttk.Label(master=window, text='Miles to Kilometers', font='Calibri 25 bold')
title_label.pack()

#input field

input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable = entry_int) # this saves the data in the entry into the entryInt
btn = ttk.Button(master=input_frame, text='Convert', command= convert)
entry.pack(side='left', padx=10)
btn.pack(side='left', padx= 10)
input_frame.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text='Output: ', font='Calibri 25 ', textvariable=output_string)
output_label.pack(pady=5)


# Run 

window.mainloop()



