import tkinter as tk
from tkinter import ttk

# setup



window = tk.Tk()
# centre the window

middle_width = window.winfo_screenwidth() 
middle_height = window.winfo_screenheight() 
window_width = 900
window_height = 600

left = int(middle_width / 2 - window_width / 2)
top = int(middle_height / 2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{left}+{top}')

window.title('pack with frames')

# Top Frame 
top_frame = ttk.Frame(window)
label1 = tk.Label(top_frame, text = 'First label', background='red')
label2 = tk.Label(top_frame, text = '2nd label', background='blue')

# middle widget
label3 = tk.Label(window, text = 'Another label', background='green')


# bottom frame left
bottom_frame1 = ttk.Frame(window)


label4 = tk.Label(bottom_frame1, text='last of the labels', background='magenta')
button = tk.Button(bottom_frame1, text = 'button')
button2 = tk.Button(bottom_frame1,text='another button')

#bottom frame on the right
bottom_frame2 = ttk.Frame(window)
button3 = tk.Button(bottom_frame2, text = 'button')
button4 = tk.Button(bottom_frame2,text='another button')
button5 = tk.Button(bottom_frame2, text = 'button')


#top layout
label1.pack(fill= 'both', expand=True)
label2.pack(fill = 'both',expand=True)
top_frame.pack(fill='both', expand=True)

#middle layout 
label3.pack(expand=True)

#bottom layout left
label4.pack(side='left', fill='both', expand=True)
button.pack(side='left', fill='both', expand=True)
button2.pack(side='left', fill='both', expand=True)
bottom_frame1.pack(side= 'left', expand=True, fill='both', pady=20, padx=20,)

# bottom layout on the right

button3.pack(side='top', fill='both', expand=True)
button4.pack(side='top', fill='both', expand=True)
button5.pack(side='top', fill='both', expand=True)
bottom_frame2.pack(side='right', expand=True,fill='both', pady=20, padx=50)



window.mainloop()