import tkinter as tk
from controllers.core_db import BBDD


if __name__ == "__main__":
    root = tk.Tk()
    data_base = BBDD()
    
    
    data_base.build()
    root.mainloop()