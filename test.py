from core import *
from commonbuild import *
from os import listdir
from os.path import isfile, expandvars
from re import compile, match
from subprocess import call

testfile_extension = ".test.py"
testfile_pattern = compile(r"([^\.]+)\.test\.py")
testfile_msg = "No {}test.py files were found"
python = "python3.7"

def write_template(f, filename):
    with open(f, "w") as f:
        with open(expandvars("$GTEST_HOME/testtemplate.py"), "r") as t:
            for l in t.readlines():
                if "$file" in l:
                    f.write(l.replace("$file", "\"./{}\"".format(filename)))
                else:
                    f.write(l)

def make_template(f, options):
    filename = c_file_pattern.match(f).group(1)
    templateFile = "{}.test.py".format(filename)

    if isfile(templateFile) and input(
            "Test file \"{}\" already exists. Overwrite [y/n]? ".format(templateFile)).lower() == "n":
        return
    else:
        write_template(templateFile, filename)
        clear_if_not_explicit(options)
        print("{} generated".format(templateFile))

def test(f, options):
    clear_if_not_explicit(options)

    print("<< " + f + " >> \n")
    call([python, f, "-v"] + (options if options else []))

if __name__ == "__main__":
    options = get_options()
    if "-t" in options:
        print("Make test template:")
        execute_with_file_options(
            c_file_pattern,
            c_file_msg,
            make_template
        )
    else:
        print("Run tests:")
        execute_with_file_options(
            testfile_pattern,
            testfile_msg,
            test
        )