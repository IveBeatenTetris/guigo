# dependencies
from . utils import (
    validateDict,
    convertColor
    )
from . import DEFAULT
import tkinter as tk

class Layout(tk.PanedWindow):
    """Basic menubar object."""
    default = DEFAULT["Layout"]
    def __init__(self, cfg={}):
        """Constructor."""
        self.cfg = validateDict(cfg, self.default)# dict
        #self.background = convertColor(self.cfg["background"])# none / str
        self.background = convertColor(self.cfg["background"])# none / str
        self.border = self.cfg["border"]# tk.constant
        self.orientation = self.cfg["orientation"]# tk.constant
        tk.PanedWindow.__init__(
            self,
            orient=self.orientation,
            background=self.background,
            relief=self.border
            )
        self.pack(fill=tk.BOTH, expand=1)
