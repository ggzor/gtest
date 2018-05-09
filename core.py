from os import listdir, system as execute
from re import compile, match, search
from subprocess import call
from sys import argv
from platform import system

def clear():
    clear_command = "clear"

    if system() == "Windows":
        clear_command = "cls"

    execute(clear_command)

def clear_if_not_explicit(options):
    if not(options and "-exp" in options):
        clear()

def try_compile(s):
    if isinstance(s, str):
        return compile(s)
    # For python 2 compatibility, we dont use isinstance(s, Pattern)
    elif "Pattern" in str(type(s)):
        return s
    else:
        raise Exception("Not a pattern or str: {}".format(str(s)))

def filter_by(values, matches, searches):
    if not isinstance(matches, list):
        matches = [matches]
    if not isinstance(searches, list):
        searches = [searches]

    matches = [try_compile(s) for s in matches]
    searches = [try_compile(s) for s in searches]

    for value in values:
        valid = True
        for m in matches:
            valid &= bool(match(m, value))
        for s in searches:
            valid &= bool(search(s, value))
        if valid:
            yield value

def args_by_filter(f):
    return [arg for arg in argv[1:] if f(arg)]

def get_options():
    return args_by_filter(lambda a: a.startswith("-") or a.startswith("./"))

def get_non_options():
    return args_by_filter(lambda a: not a.startswith("-") and not a.startswith("./"))

def get_firstmatch(filename, pattern):
    pattern = try_compile(pattern)
    with open(filename) as f:
        for line in f.readlines():
            m = match(pattern, line)
            if m:
                return m
    return None

def read_option(options, optionformatter=None):
    count = len(options)

    for i, option in zip(range(1, count + 1), options):
        value = optionformatter(option) if optionformatter else str(option)        
        print("{}{}.- {}".format(" " * 4, i, value))

    option = input("Option: ")
    if option:
        try:
            index = int(option)
            if 1 <= index <= count:
                return options[index - 1]
            else:
                print("Index out of range")
        except ValueError:
            print("Not as number")
    else:
        print("No option was given")

def execute_with_file_options(matches, msg, func, formatter=None):
    searches = get_non_options()
    options = get_options()

    # using listdir(".") instead of single listdir() for python 2 compatibility
    files = list(sorted(filter_by(listdir("."), matches, searches)))
    
    if files:
        if len(files) == 1:
            selected = files[0]
        else:
            selected = read_option(files,formatter)
        
        if selected:
            func(selected, options)
    else:
        print(msg.format("matching " if searches else ""))