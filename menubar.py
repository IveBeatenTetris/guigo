# dependencies
from . utils import validateDict
from . import DEFAULT
import tkinter as tk

class MenuBar(tk.Menu):
    """Basic menubar object."""
    default = DEFAULT["MenuBar"]
    def __init__(self, master=None, cfg={}):
        """Constructor."""
        tk.Menu.__init__(self, master, tearoff=0)
        self.cfg = validateDict(cfg, self.default)# dict
        self.master = master# tk.master
        # filemenu = tk.Menu(self, tearoff=0)
        # filemenu.add_command(label="Open", command=helloWorld)
        # self.add_cascade(label="Current", menu=filemenu)
        self._build()
    def _build(self):
        """
        Dynamically create submenus from config and add them to the menubar.
        """
        for each in self.cfg["constructor"]:
            submenu = tk.Menu(self, tearoff=0)

            for op in each["options"]:
                submenu.add_command(label=op["name"])

            self.add_cascade(label=each["name"], menu=submenu)

def helloWorld(test):
    print(test)
