import tkinter as tk
from tkinter import ttk

# setup

window = tk.Tk()
window.geometry('600x400')
window.title()

# Noteboook

notebook = ttk.Notebook(window)
tab1 = ttk.Frame(notebook)

label1 = ttk.Label(
    tab1,
    text='click on tab2'
)
label1.pack()

tab2 = ttk.Frame(notebook)

label2 = ttk.Label(
    tab2,
    text='you are cool'
)
label2.pack()

tab3 = ttk.Frame(notebook)

btn = ttk.Button(
    tab3,
    text='yes'
)

btn.pack()

label3 = ttk.Label(
    tab3,
    text='Fred salle is the best'
)

label3.pack()




notebook.add(tab1, text= 'tab1')
notebook.add(tab2, text= 'tab2')
notebook.add(tab3, text='tab3')
notebook.pack()


window.mainloop()