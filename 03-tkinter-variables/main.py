import tkinter as tk
from tkinter import ttk

def button_func():
    # get the content of the entry
    entry_text = entry.get()
    
    #update label   
    label['text'] = entry_text
    entry['state'] = 'disabled'
    # this prints all of the possible things u can do with a widget – print(label.configure()) 
    
def change_btn():
    label['text'] = 'Some text'
    entry['state'] = 'enabled'

# window
window = tk.Tk()
window.title('Getting and Setting widgets')
# 👇 This makes the window always on top (until you remove it)
window.attributes('-topmost', 1)


#widgets
label = ttk.Label(master=window, text='Some text', font='Calibri 25 bold')
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text='Click me for free money', command=button_func)
button.pack()

newBtn = ttk.Button(master=window, text='change label to original', command=change_btn)
newBtn.pack()

#run 
window.mainloop()


