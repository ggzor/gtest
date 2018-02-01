#!/bin/bash
if [ -z ${GTEXT_HOME+x} ]
then python ./test.py $@
else python "$GTEST_HOME/test.py" $@
fi