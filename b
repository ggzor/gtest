#!/bin/bash
if [ -z ${GTEST_HOME+x} ]
then python ./build.py $@
else python "$GTEST_HOME/build.py" $@
fi