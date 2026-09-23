import tkinter as tk
from tkinter import ttk
import webbrowser


# setup

window = tk.Tk()
window.geometry('600x400')
window.title('Menu')

# You use tk.Menu within a tk.Menu

# menu 
menu = tk.Menu(window)
 
# sub menu
file_menu = tk.Menu(menu)
file_menu.add_command(label='New File', command= lambda: print('New file'))
file_menu.add_separator()
file_menu.add_command(label='Open File', command= lambda: print('Open file'))

menu.add_cascade(label = 'File', menu = file_menu)

# another sub menu

help_menu = tk.Menu(menu)
help_menu.add_command(label='Click for help', command= lambda: print(help_check_string.get()))

help_check_string = tk.StringVar()
help_menu.add_checkbutton(label='check', onvalue='on', offvalue='off', variable=help_check_string)

menu.add_cascade(label='Help', menu=help_menu)

website_menu = tk.Menu(menu)
menu.add_cascade(label='click to be redirected', menu=website_menu)


link_menu = tk.Menu(website_menu)
link_menu.add_command(label='Click to be actually actually redirected HAHAHHAHAH ', command=lambda: webbrowser.open('https://www.youtube.com/watch?v=mop6g-c5HEY&t=3756s') )

website_menu.add_cascade(label='Click to be actually  redirected  ', menu=link_menu)


window.configure(menu = menu)






menu_button = ttk.Menubutton(window, text='Menu Button')
menu_button.pack()

button_sub_menu = tk.Menu(menu_button)
button_sub_menu.add_command(label = 'entry 1', command=lambda: print('test 1'))
menu_button.configure(menu = button_sub_menu)

window.mainloop() 