import tkinter as tk
from tkinter import ttk

# setup

window = tk.Tk()
# centre the window

middle_width = window.winfo_screenwidth() 
middle_height = window.winfo_screenheight() 
window_width = 1400
window_height = 800

left = int(middle_width / 2 - window_width / 2)
top = int(middle_height / 2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{left}+{top}')
window.minsize(600,600)
window.title('lesgooo')
style = ttk.Style()
style.theme_use('classic') 

# frames

left_frame = ttk.Frame(window)
left_frame_check = ttk.Frame(window)
right_frame = ttk.Frame(window)
right_left_frame = ttk.Frame(right_frame)
right_right_frame = ttk.Frame(right_frame)


#left frame widgets
btn1 = ttk.Button(left_frame, text='Btn')
btn2 = ttk.Button(left_frame, text='Btn2')
btn3 = ttk.Button(left_frame, text='Btn3')

slider1 = ttk.Scale(left_frame, orient='vertical')
slider2 = ttk.Scale(left_frame, orient='vertical')

# left frame layout

left_frame.columnconfigure((0,1,2), weight=1, uniform= 'a')
left_frame.rowconfigure((0,1,2,3,4), weight= 1, uniform='a')

btn1.grid(column=0, row=0, sticky='nesw', columnspan=2)
btn2.grid(column=2, row=0, sticky='nesw')
btn3.grid(column=0, row=1, sticky='nesw', columnspan=3)

slider1.grid(column=0, row = 2, sticky='ns', rowspan=2, pady=20)
slider2.grid(column=2,row=2, sticky='ns', rowspan=2, pady=20)


#toggle layout

left_frame_check = ttk.Frame(left_frame)
check_box1 = ttk.Checkbutton(left_frame_check, text='check 1')
check_box2 = ttk.Checkbutton(left_frame_check, text='check 2')
entry = ttk.Entry(left_frame)

left_frame_check.grid(row = 4, column= 0, columnspan=3, sticky='nswe')


check_box1.pack(side='left', expand=True)
check_box2.pack(side='right', expand=True)

lbl1 = ttk.Label(right_left_frame, text='lbl1', background='magenta',anchor='center')
btn4 = ttk.Button(right_left_frame, text='Btn3')

lbl2 = ttk.Label(right_right_frame, text='lbl2', background='violet',anchor='center')
btn5 = ttk.Button(right_right_frame, text='Btn5')

# right left frame layout
lbl1.pack(expand=True, fill='both')
btn4.pack(expand=True, fill='both')
lbl2.pack(expand=True, fill='both')
btn5.pack(expand=True, fill='both')

#entry layout

entry.place(relx=0.5, rely=0.98, anchor='center')

# frame layout
left_frame.place(relx=0, rely=0, relwidth=0.3, relheight=1)
right_frame.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
right_left_frame.pack(side='left', expand=True, fill='both', padx= 20, pady=20)
right_right_frame.pack(side='right', expand=True, fill='both', padx=20, pady=20)



# left frame widget layout



window.mainloop() 