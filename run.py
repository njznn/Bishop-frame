import numpy as np
import ctypes as C
from bishop_gui import *



### run
root = tk.Tk()
app = App(root)
root.title("BISHOP FRAME OF THE CURVE")
root.mainloop()
root.protocol("WM_DELETE_WINDOW", on_closing)