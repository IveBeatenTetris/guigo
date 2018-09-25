from tkinter import *

# lib constants
DEFAULT = {
    "Window": {
        "size": (640, 480)
    },
    "MenuBar": {
        "size": (100, 100),
        "constructor": [
            {
                "name": "File",
                "options": [
                    {
                        "name": "Open",
                        "operation": "open()",
                    },
                    {
                        "name": "Save",
                        "operation": "save()",
                    },
                    {
                        "name": "Exit",
                        "operation": "exit()",
                    }
                ]
            },
            {
                "name": "Edit",
                "options": [
                    {
                        "name": "Copy",
                        "operation": "copy()",
                    },
                    {
                        "name": "Cut",
                        "operation": "cut()",
                    },
                    {
                        "name": "Paste",
                        "operation": "paste()",
                    }
                ]
            },
            {
                "name": "Run",
                "options": [
                    {
                        "name": "Run",
                        "operation": "run()",
                    }
                ]
            },
            {
                "name": "Help",
                "options": [
                    {
                        "name": "About",
                        "operation": "about()",
                    },
                    {
                        "name": "Info",
                        "operation": "info()",
                    },
                    {
                        "name": "Test",
                        "operation": "test()",
                    }
                ]
            }
        ]
    },
    "Layout": {
        "align": "nw",
        "background": None,
        "border": None,
        "orientation": HORIZONTAL
    }
}

# dependencies
from .utils import *
from .window import Window
from .layout import Layout
from .menubar import MenuBar
