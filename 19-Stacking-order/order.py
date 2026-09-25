import tkinter as tk
from tkinter import ttk

# setup

def raise_lbl1():
    lbl1.lift()
    
def raise_lbl2():
    lbl2.lift()


window = tk.Tk()
# centre the window

middle_width = window.winfo_screenwidth() 
middle_height = window.winfo_screenheight() 
window_width = 400
window_height = 400

left = int(middle_width / 2 - window_width / 2)
top = int(middle_height / 2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{left}+{top}')

window.title('stacking order')

lbl1 = tk.Label(window, text='lbl 1', background='blue')
lbl2 = tk.Label(window, text='lbl 2', background='orange')
lbl3 = tk.Label(window, text='lbl 3', background='green')

btn1 = tk.Button(window, text= 'raise lbl1', command=raise_lbl1)
btn2 = tk.Button(window, text= 'raise lbl2', command=raise_lbl2)
btn3 = tk.Button(window, text= 'raise lbl3', command=lambda : lbl3.lift())

# layout

lbl1.place(anchor='center', relx=0.4, rely=0.4, relwidth=0.2, relheight=0.3)
lbl2.place(anchor='center', relx=0.5, rely=0.6, relwidth=0.2, relheight=0.3)
lbl3.place(anchor='center', relx=0.4, rely=0.5, relwidth=0.2, relheight=0.3)

btn1.place(anchor='se', relx=1, rely=1)
btn2.place(anchor='se', relx=1, rely=0.95)
btn3.place(anchor='se', relx=1, rely=0.85)

#run 
window.mainloop()