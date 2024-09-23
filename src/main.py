import tkinter as tk
from models.db_connection import BBDD
from views.base_view import BaseView


if __name__ == "__main__":
    root = tk.Tk()
    data_base = BBDD()
    BaseView(root)
    
    data_base.build()
    root.mainloop()