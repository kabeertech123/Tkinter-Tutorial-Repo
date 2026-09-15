import tkinter as tk
from tkinter import ttk


def button_func(entry_string):
    print("a button was pressed")
    print(entry_string.get())


# setup
window = tk.Tk()
window.title("buttons, functions & arguments")

# widgets
entry_string = tk.StringVar(value="test")
entry = ttk.Entry(window, textvariable=entry_string)
entry.pack()

button = ttk.Button(window, text="button", command=lambda: button_func(entry_string))
# The function returns NONE which results to nothing happening when the button is being pressed so we need the lambda
# you can use the outer inner function shown in the ss lambda is easier to use.
button.pack()

# run
window.mainloop()
