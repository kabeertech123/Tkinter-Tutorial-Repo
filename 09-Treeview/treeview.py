import tkinter as tk
from tkinter import ttk
from random import choice

# setup

window = tk.Tk()
window.geometry('600x400')
window.title('Treeview')

first_names = [
    'Alice', 'Bob', 'Charlie', 'Diana', 'Ethan',
    'Fiona', 'George', 'Hannah', 'Ivan', 'Julia'
]

last_names = [
    'Smith', 'Johnson', 'Williams', 'Brown', 'Jones',
    'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez'
]

#tree view

table = ttk.Treeview(window, columns=('first', 'last', 'email'), show='headings')
table.heading('first', text='First name')
table.heading('last', text='Last name')
table.heading('email', text='Email')
table.pack(fill='both', expand=True)

# insert values into a table
# table.insert(parent='', index= 0, values=('John', 'Doe', 'JohnDoe@gmail.com'))

for i in range(10):
    first = first_names[i]
    last = last_names[i]     
    #first = choice(first_names)
    #last = choice(last_names) randomly chooses a first name and a last name from their respective arr 
    email = f'{first[0]}{last}@gmail.com'
    data = (first, last, email)
    table.insert(parent='', index=0, values= data)
    # a tuple can hold different data types and they are immutable meaning you can't change the contents once created
    
table.insert(parent='', index=tk.END, values=('xxxx','yyyyy','zzzz')) # index is where the data will be stored in the table 

# events
def item_select(_):
    for i in table.selection():
        print(table.item(i)['values'])
        
def delete_items(_):
    print('delete')
    for i in table.selection():
        table.delete(i)
    
    
table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_items)

# items



window.mainloop()