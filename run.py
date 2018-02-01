from core import *
from re import compile
from subprocess import call

executable_file_pattern = compile(r"^[^\.]+$")
executable_file_msg = "No {}executable files found"

def run(file, options):
    return call(["./" + file])  

def make_run(file, options):
    print("Starting {}".format(file))

    clear_if_not_explicit(options)
    
    exitcode = run(file, options)

if __name__ == "__main__":
    execute_with_file_options(executable_file_pattern, executable_file_msg, make_run)