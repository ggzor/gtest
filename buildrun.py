from core import execute_with_file_options
from commonbuild import c_file_pattern, c_file_msg, format_fileoptions
from build import make_build
from run import make_run

def buildrun(file, options):
    if make_build(file, options):
        return
    else:
        make_run(file[:-2], options)

if __name__ == "__main__":
    execute_with_file_options(c_file_pattern, c_file_msg, buildrun, format_fileoptions)