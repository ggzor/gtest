#!/bin/bash
if [ -z ${GTEST_HOME+x} ]
then python ./run.py $@
else python "$GTEST_HOME/run.py" $@
fi