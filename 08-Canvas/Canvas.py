import tkinter as tk
from tkinter import ttk

# setup

window = tk.Tk()
window.geometry('600x400')
window.title('Canvas')

# canvas

canvas = tk.Canvas(window, bg= 'white')
canvas.pack()    

canvas.create_rectangle((50,20, 100, 200), fill='red', width=10, outline='green') # (left, top, right, bottom) is the format
canvas.create

window.mainloop()