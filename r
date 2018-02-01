#!/bin/bash
if [ -z ${GTEXT_HOME+x} ]
then python ./run.py $@
else python "$GTEST_HOME/run.py" $@
fi