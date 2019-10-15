Homework 5: Time Series

This assignment contains classes & functions to read and round time series data from CSV files. It also finds and matches data values at each timestamp. I did not finish the assignment. The information below details what I was able to finish.
I don't think I followed the correct local branching either. I wrote the functions in separate branches on my local repo but somehow I ended up with just 1 local master that I pushed back to the remote master.

Usage
The `data_import.py` program is the main program of the assignment. Its parameters are detailed below.
The `data_import_test.py` program contains a unit test for the `ImportData` class within `data_import.py`. I only wrote 1 unit test because the other functions are not working properly.

`ImportData` Class
    This class imports CSV time,value data from a specified file in the smallData directory and makes arrays of the times and data values. It also contains a linear_search_value to find & return an array of data values associated with a specific time.

`roundTimeArray` Function
    This function rounds the timestamps found in the `ImportData` class to the nearest 5-minute value. It also chooses the values matched with each rounded timestamp and makes a zipped iterable of (rounded time, value) pairs.
    
I was not able to write the `printLargeArray` function. `data_import.py` exits after running the `roundTimeArray` function. The `data_import.py` program has no output.
I also did not understand the key_time terminology in the `roundTimeArray` and `linear_search_value` functions and I do not think these functions are working properly.

The `.travis.yml` file calls the `time_series_tests.sh` shell script to run unit & functional tests on `data_import.py` and to run `pycodestyle` on `data_import_test.py` and `data_import_test.py`.
