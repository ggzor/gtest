from commonbuild import *
from core import *
from subprocess import call

def build(file, options):
    return call(["gcc", file, "-o", file[:-2]] + ([options] if options else []))

def make_build(file, options):
    clear_if_not_explicit(options)

    fileoptions = get_fileoptions(file)

    print("Compiling {}{}...".format(file, " " + fileoptions if fileoptions else ""))

    b = build(file, fileoptions)

    if b:
        print("Compilation failed")
    else:
        print("Done")
    
    return b

if __name__ == "__main__":
    execute_with_file_options(
        c_file_pattern, 
        c_file_msg, 
        make_build,
        format_fileoptions
    )