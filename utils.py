# dependencies
import tkinter as tk
# dictionary operations
def validateDict(config={}, defaults={}):# dict
    """Validate a dictionary by given defaults. Params must be dict."""
    validated = {}

    for each in defaults:
        try:
            validated[each] = config[each]
        except KeyError:
            validated[each] = defaults[each]

    return validated
def convertColor(value):
    """Convert the value into tk's color value and return it."""
    if value is None:
        color = None
    elif type(value) is tuple:
        color = "#%02x%02x%02x" % value
    else:
        color = value

    return color
