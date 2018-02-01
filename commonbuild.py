from core import get_firstmatch
from re import compile

options_pattern = compile(r"// +build +(.+)")

c_file_pattern = compile(r"([^\.]+)\.c")
c_file_msg = "No {}C files were found"

def get_fileoptions(filename):
    m = get_firstmatch(filename, options_pattern)   
    f = m.group(1) if m else None 
    if m and f:
        return f

def format_fileoptions(o):
    options = get_fileoptions(o)
    return "{} {}".format(o, "({})".format(options) if options else "")