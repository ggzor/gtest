from core import clear_if_not_explicit, execute_with_file_options, get_firstmatch
from commonbuild import c_file_pattern, c_file_msg, format_fileoptions
from build import make_build
from test import test, testfile_extension
from re import compile, match
from os import listdir

options_pattern = compile(r"// +buildtest +(.+)")

def find_file(s):
    for f in listdir("."):
        if f == s:
            return f

def get_fileoptions(f):
    m = get_firstmatch(f, options_pattern)
    f = m.group(1) if m else None
    if m and f:
        return f

def buildtest(file, options):
    if make_build(file, options):
        return
    else:
        m = match(c_file_pattern, file)
        f = m.group(1) if m else None
        if m and f:
            testfile = f + testfile_extension

            to_run = find_file(testfile)

            clear_if_not_explicit(options)

            if to_run == None:
                reference = get_fileoptions(file)
                to_run = find_file(reference)
                if to_run == None:
                    print("\"{}\" was not found.".format(reference))
                    return

            if to_run:
                test(to_run, options + ["./" + f])
            else:
                print("No test file for \"{}\" was found.".format(file))

if __name__ == "__main__":
    execute_with_file_options(c_file_pattern, c_file_msg, buildtest, format_fileoptions)