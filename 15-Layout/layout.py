import tkinter as tk
from tkinter import ttk

# setup 

window = tk.Tk()

# centre the window
middle_width = window.winfo_screenwidth() 
middle_height = window.winfo_screenheight() 
window_width = 600
window_height = 400

left = int(middle_width / 2 - window_width / 2)
top = int(middle_height / 2 - window_height / 2)

window.geometry(f'{window_width}x{window_height}+{left}+{top}')

window.configure(bg='white')

window.title('layout')


# widgets

label1 = tk.Label(window, text='hello', background='green')
label2 = tk.Label(window, text='hi', background='blue')

#pack
#label1.pack(side = 'left', expand=True, fill='both')
#label2.pack(side = 'left', expand=True, fill='both')

# grid 

#window.columnconfigure(0, weight = 1) # first num represents the index
#window.columnconfigure(1, weight= 1)
#window.columnconfigure(2, weight= 2) #2x as wide
#window.rowconfigure(0, weight=1)
#window.rowconfigure(1, weight=1)


#label1.grid(row = 0, column= 1, sticky='nsew')
#label2.grid(row = 1, column= 1, columnspan=2, sticky='nsew')

#place 
label1.place(x = 110, y = 200, width=200, height=100)
label2.place(relx = 0.5 , rely=0.5, relwidth=1, anchor= 'center') # will always keep the label in the middle


window.mainloop()