import tkinter as tk
from tkinter import ttk

class App(tk.Tk): # Creates an App class that inherits from tk.Tk
    def __init__(self, title, minsize):
        
        # main setup
        super().__init__() # Run the initialization method of the class im inheriting from
        self.title(title) # these aren't objects, rather its a method. Its an attribute to the app object
        self.geometry(f'{minsize[0]}x{minsize[1]}')
        self.minsize(minsize[0], minsize[1])
        self.style = ttk.Style()
        self.style.theme_use('classic')
    
        # Widgets
        self.menu = Menu(self) # Creates a menu object 
        self.main = Main(self)   
        
       

        self.mainloop()    
        
class Menu(ttk.Frame): # Menu inherites from ttk.Frame
    def __init__(self, parent): # parent is the window, nothing to do with inheritance
        super().__init__(parent)
        #ttk.Label(self,background='red').pack(expand=True, fill='both')
        self.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        
        self.create_widgets()

    def create_widgets(self):
        
        # create widgets
        btn1 = ttk.Button(self, text='Btn')
        btn2 = ttk.Button(self, text='Btn2')
        btn3 = ttk.Button(self, text='Btn3')

        slider1 = ttk.Scale(self, orient='vertical')
        slider2 = ttk.Scale(self, orient='vertical')
        left_frame_check = ttk.Frame(self)
        check_box1 = ttk.Checkbutton(left_frame_check, text='check 1')
        check_box2 = ttk.Checkbutton(left_frame_check, text='check 2')
        entry = ttk.Entry(self)

        # create grid
        self.columnconfigure((0,1,2), weight=1, uniform= 'a')
        self.rowconfigure((0,1,2,3,4), weight= 1, uniform='a')

        # placing widgets 
        
        btn1.grid(column=0, row=0, sticky='nesw', columnspan=2)
        btn2.grid(column=2, row=0, sticky='nesw')
        btn3.grid(column=0, row=1, sticky='nesw', columnspan=3)

        slider1.grid(column=0, row = 2, sticky='ns', rowspan=2, pady=20)
        slider2.grid(column=2,row=2, sticky='ns', rowspan=2, pady=20)
        
        left_frame_check.grid(row = 4, column= 0, columnspan=3, sticky='nswe')

        check_box1.pack(side='left', expand=True)
        check_box2.pack(side='right', expand=True)

class Main(ttk.Frame):
    def __init__(self, parent): # parent is the window, nothing to do with inheritance
            super().__init__(parent)
            #ttk.Label(self,background='red').pack(expand=True, fill='both')
            self.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
            
            self.create_widget()
            
    def create_widget(self):
        right_left_frame = ttk.Frame(self)
        right_right_frame = ttk.Frame(self)
        
        lbl1 = ttk.Label(right_left_frame, text='lbl1', background='magenta',anchor='center')
        btn4 = ttk.Button(right_left_frame, text='Btn3')
        lbl2 = ttk.Label(right_right_frame, text='lbl2', background='violet',anchor='center')
        btn5 = ttk.Button(right_right_frame, text='Btn5')

        # right left frame layout
        lbl1.pack(expand=True, fill='both')
        btn4.pack(expand=True, fill='both')
        lbl2.pack(expand=True, fill='both')
        btn5.pack(expand=True, fill='both')
        
        right_left_frame.pack(side='left', expand=True, fill='both', padx= 20, pady=20)
        right_right_frame.pack(side='right', expand=True, fill='both', padx=20, pady=20)
            
        
        
App('Class based app', (1400,800))