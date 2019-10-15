#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest
# Download testing framework.

run test_style pycodestyle data_import.py
assert_no_stdout
run test_style pycodestyle data_import_test.py
assert_no_stdout
# Run pycodestyle on data_import.py- assert these both pass with no style errors.

run roundTimeArray_function_test python data_import.py --folder_name smallData --output_file test.txt --sort_key cgm_small.csv
assert_stdout
assert_exit_code 0
# Run data_import.py on the 'cgm_small.csv' file, as required by the assignment. Assert the script 
# has stdout and exits with 0.