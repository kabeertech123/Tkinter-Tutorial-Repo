 # An event can be keyboard inputs, Widgets getting changes, widgets being selected/unselected, Mouse click/motion wheel etc
 
 # These events can be observed and used, e.g. run a function on a button press
 
 # We use Widget.bind(event,function)
 
 
import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f'z{event.x} y {event.y}')

# window
window = tk.Tk()
window.geometry('600x500')

#widgets 
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window, text = 'A button') 
btn.pack()

# Events

#btn.bind('<Command-KeyPress-a>', lambda event : print('an event'))
#text.bind('<Motion>', get_pos)
#window.bind('<KeyPress>', lambda event: print(f'{event.char} button was pressed'))
#entry.bind('<FocusOut>', lambda event: print('entry field was selected'))

# exercise
# print 'Mousewheel' when the user holds down shift and uses the mosue wheel while text is selected


text.bind('<Shift-MouseWheel>', lambda event: print('Mousewheel') )

#run
window.mainloop()