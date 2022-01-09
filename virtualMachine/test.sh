#!/bin/bash

# Trigger all your test cases with this script

echo -e -n '\x00\x00\x25\x42' >> test1.x2017

#!/bin/bash

# Trigger all your test cases with this script

echo "##########################"
echo "### Testing timetable.c"
echo "##########################\n"
count=0 # number of test cases run so far
# Assume all `.in` and `.out` files are located in a separate `tests` directory
for test in tests/*.x2017; do
name=$(basename $test .x2017)
expected=tests/$name.out

args="./vm_x2017 tests/$name.x2017"
eval $args | diff - $expected || echo "Test $name: failed!\n"
count=$((count+1))
done
echo "Finished running $count tests!"




