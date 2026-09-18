import tkinter as tk
from tkinter import ttk

# setup

window = tk.Tk()
window.geometry('600x400')
window.title('exercise for frames')

frame = ttk.Frame(
    window,
    width=200,
    height=200,
    relief=tk.GROOVE # Adds a border to the frame
    )
frame.pack_propagate(False) 
frame.pack(side='right') 

label1 = ttk.Label(
    frame,
    text="I hope Marc's voice gets better"
    
)
label1.pack()

btn = ttk.Button(
    frame,
    text='this is a btn'
)
btn.pack()

entry = ttk.Entry(
    window,
    
)
entry.pack()



window.mainloop()