import tkinter as tk
from tkinter import ttk

# Setup
window = tk.Tk()
# Centre the window
middle_width = window.winfo_screenwidth()
middle_height = window.winfo_screenheight()
window_width = 400
window_height = 600

left = int(middle_width / 2 - window_width / 2)
top = int(middle_height / 2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{left}+{top}')

window.title('place')



style = ttk.Style()
style.configure('T', foreground="red")


# Apply background color to labels
label1 = tk.Label(window, text="First label", background="red")
label2 = tk.Label(window, text="2nd label", background="orange")
label3 = tk.Label(window, text="3rd label", background="green")
button = tk.Button(window, text="btn1", )

# Pack the widgets
#label1.place(x = 300, y = 100, width= 100, height= 200)
label2.place(relx=0.2, rely=0.1, relwidth= 0.4, relheight=0.5)
label3.place(x = 79, y = 60, width= 100, height= 200)
button.place(relx=1, rely=1, anchor="se")# sets the pos of where the widget will be which is the bottom right

# frame

frame = ttk.Frame(window)
frame_label = tk.Label(frame, text = 'Frame label', background='blue')
frame_button = tk.Button(frame, text = 'Frame label')

# layout
frame.place(relx = 0, rely= 0, relwidth=0.3, relheight=1)
frame_label.place(relx=0, rely=0, relwidth=1, relheight= 0.5)
frame_button.place(relx = 0, rely=0.5, relwidth=1, relheight= 0.5)


# Run the application
window.mainloop()