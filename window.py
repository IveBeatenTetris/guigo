# dependencies
from . utils import validateDict
from . menubar import MenuBar
from . import DEFAULT
import tkinter as tk

class Window(tk.Tk):
    """Basic window object."""
    default = DEFAULT["Window"]
    def __init__(self, cfg={}):
        """Constructor."""
        tk.Tk.__init__(self)
        self.cfg = validateDict(cfg, self.default)# dict
        self.size = self.cfg["size"]# tuple
        self.resize(self.size)
    def add(self, element):
        """Add given element to the window."""
        if type(element) is MenuBar:
            self.config(menu=element)
    def resize(self, size):
        """Resize the window. 'size' must be (int, int)."""
        self.geometry('{}x{}'.format(size[0], size[1]))
    def update(self):
        """Tk's update-function."""
        tk.mainloop()
