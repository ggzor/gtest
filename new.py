from sys import argv
from os.path import expandvars, join
from os import getcwd
from shutil import copy

def make_new(filename):
    template = join(expandvars("$GTEST_HOME"), "ctemplate.c")

    if not filename.endswith(".c"):
        filename += ".c"

    copy(template, filename)

if __name__ == "__main__":
    if len(argv) > 1:
        make_new(join(getcwd(), argv[1]))
    else:
        print("Usage: n <file>")