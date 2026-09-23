import tkinter as tk
from tkinter import ttk

# setup


window = tk.Tk()

window.geometry('600x400+100+500')
window.title('change the window')
window.iconbitmap('aizen.ico')


# start window in the middle of screen



# window sizes
#window.minsize(500,500)
# window.maxsize(800,700) 
# window.resizable(True, False)

#screen attributes

print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# window attributes
window.attributes('-alpha', 1) # changes transparancy 
#window.attributes('-topmost',True ) # places the app first then vs code  

#window.attributes('-fullscreen', True)

window.bind('<x>', lambda event: window.quit())


# title bar
window.overrideredirect(True)
grip = ttk.Sizegrip(window)
grip.place(relx = 1.0, rely= 1.0, anchor='se')

window.mainloop()