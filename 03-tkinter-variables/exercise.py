import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Variable Exercise')
window.geometry('500x200')

# 👇 This makes the window always on top (until you remove it)
window.attributes('-topmost', 1)

string_var = tk.StringVar(value='test')

label = ttk.Label(master=window, text='test', textvariable=string_var)
label.pack()

entry1 = ttk.Entry(master=window, textvariable=string_var)
entry1.pack()

entry2 = ttk.Entry(master=window, textvariable=string_var)
entry2.pack()



#run
window.mainloop()




