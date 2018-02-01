import sys
import os
sys.path.append(os.path.expandvars("$GTEST_HOME"))

import unittest
import process
from util import get_file
from sys import argv

(args, f) = get_file(argv, $file)

class Tests(unittest.TestCase):
    def r(self, *params):
        return process.run(f, *params).split("\n")

    ###
    ### YOUR TESTS GO HERE
    ###

    def test_nothing(self):
        self.fail("Here go the tests for {}".format($file))

unittest.main(argv=args)
