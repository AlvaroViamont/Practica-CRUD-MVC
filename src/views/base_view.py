import tkinter as tk
from tkinter import ttk


class BaseView:
    def __init__(self, root:tk.Tk) -> None:
        
        self.COLOR_OXFORD_BLUE = '#000022'
        self.COLOR_SNOW = '#FBF5F3'
        self.PAYNES_GRAY = '#4F6367'
        self.COLOR_JUNGLE_GREEN = '#00B295'
        self.COLOR_CARDINAL = '#C42847'
        
        self.TITLE_FONT = ("Arial", 24, "bold") 
        self.SUBTITLE_FONT = ("Arial", 16, "bold") 
        self.BODY_FONT = ("Arial", 12) 
        self.BUTTON_FONT = ("Arial", 12, "bold")
        self.HIGHLIGHT_FONT = ("Arial", 16, "bold")  
        self.FOOTNOTE_FONT = ("Arial", 10, "bold") 
        
        self.root = root
        self.root.configure(background=self.COLOR_OXFORD_BLUE)
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.root.bind('<Escape>', lambda event: self.root.state('normal'))
        self.root.bind('<F11>', lambda event: self.root.state('zoomed'))
        self.root.state('zoomed')
        
        self.top_frame = tk.Frame(self.root, bg=self.COLOR_OXFORD_BLUE)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        self.bottom_frame = tk.Frame(self.root, bg=self.PAYNES_GRAY)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        
        self.product_button = tk.Button(self.top_frame, text='Producto', foreground=self.COLOR_SNOW, activeforeground=self.COLOR_CARDINAL, bg=self.COLOR_CARDINAL, activebackground=self.COLOR_SNOW, font=self.SUBTITLE_FONT)
        self.product_button.pack(side=tk.LEFT, ipadx=10, ipady=10, pady=1)
        self.category_button = tk.Button(self.top_frame, text='Categoría', foreground=self.COLOR_SNOW, activeforeground=self.COLOR_CARDINAL, bg=self.COLOR_CARDINAL, activebackground=self.COLOR_SNOW, font=self.SUBTITLE_FONT)
        self.category_button.pack(side=tk.LEFT, ipadx=10, ipady=10, padx=1, pady=1)
        