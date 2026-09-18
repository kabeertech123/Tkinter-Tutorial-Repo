import tkinter as tk
from tkinter import ttk

# setup

window = tk.Tk()
window.geometry('600x400')
window.title('frames')

# frames are just divs in tkinter
# we just place widgets in frames

#frame 
frame = ttk.Frame(
    window, 
    width=200,
    height=200, # ttk sets the size of its frames by its children so the hight and width will change
    borderwidth=10,
    relief=tk.GROOVE # Adds a border to the frame
)
frame.pack_propagate(False) # this ensures that the height and width stays the same
frame.pack() # if you move this to the bottom, then label2 will be displayed first

# master setting

label = ttk.Label(
    master=frame,
    text='label in frame'
)
label.pack()

btn = ttk.Button(
    frame,
    text='i am in the frame and i love King Sam'
)
btn.pack()

# example

label2 = ttk.Label(
    window,
    text='label OUTSIDE frame'
) 
label2.pack()

#frame.pack() 

window.mainloop() 