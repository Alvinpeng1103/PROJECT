#!/bin/bash

# Trigger all your test cases with this script

echo "##########################"
echo "### Testing timetable.c"
echo "##########################\n"



count=0 # number of test cases run so far
# Assume all `.in` and `.out` files are located in a separate `tests` directory
for test in testcases/*.expected; do
name=$(basename $test .expected)
expected=testcases/$name.expected
actual=testcases/$name.out
args="./tests.c"
diff  $expected $actual || echo "Test $name: failed!\n"
count=$((count+1))
done
echo "Finished running $count tests!"