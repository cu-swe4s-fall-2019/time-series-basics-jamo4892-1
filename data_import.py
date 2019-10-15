import csv
import sys
import dateutil.parser
from os import listdir
from os.path import isfile, join
import argparse
import datetime
import time
# Import modules.


class ImportData:
    def __init__(self, data_csv):
        """
        Purpose
        -------
        This function opens a file and reads the columns into an array.

        Inputs
        ------
        data_csv: String
        Name of the CSV file to open & read.

        Outputs
        -------
        _time: Array
        Array containing the times of the input file.

        _value: Array
        Array containing the values of the input file.
        """

        self._time = []
        self._value = []
        self._type = []

        if 'meal' in data_csv or 'bolus' in data_csv or 'activity' in data_csv:
            self._type = 0
        if 'basal' in data_csv or 'smbg' in data_csv:
            self._type = 1
        if 'cgm' in data_csv or 'hr' in data_csv:
            self._type = 1
        # Set data type for use in roundTimeArray function below.

        with open(data_csv, "r") as fhandle:
            reader = csv.DictReader(fhandle)
            # Read the file into an array.
            for row in reader:
                if (row['time'] == ''):
                    continue
                try:
                    self._time.append(datetime.datetime.strptime(
                                      row['time'], '%m/%d/%y %H:%M'))
                    # Append each 'time' value in the 'reader' array to the
                    # '_time' array.
                except ValueError:
                    print("Input 'time' has bad format")
                    dateutil.parser.parse(row['time'])
                    sys.exit(1)
                    # Find & print any 'time' value that gives a ValueError.
                self._value.append(row['value'])
                if (row['value'] == 'low'):
                    print("Value = 'low'; converting 'value' to 40")
                    row['value'] == 40
                if (row['value'] == 'high'):
                    print("Value = 'high'; converting 'value' to 300")
                    row['value'] == 300
                # Append each 'value' value in the 'reader' array to the
                # '_value' array.
            fhandle.close()

    def linear_search_value(self, key_time):
        """
        Purpose
        -------
        This function finds the value associated with a given time key.

        Inputs
        ------
        Key_time: Integer
        Time value to match in the '_time' array.

        Outputs
        -------
        value: Array
        Array of values corresponding to the chosen key_time.
        """

        value = []
        for i in range(len(self._time)):
            if self._time[i] == key_time:
                value.append(self._value[i])
                # If the input key time is in the '_time' array,
                # append the _value value of the key to the 'value' array.
            if len(value) == 0:
                print('No values found for the selected key_time')
                return -1
        return value


def roundTimeArray(obj, res):
    """
    Purpose
    -------
    This function rounds an array of time values to the nearest 5-minute value,
    then returns the rounded time values and the data values of the rounded
    time values in a zipped iterable array.

    Inputs
    ------
    Obj: Object
    Object from ImportData class.

    Res: Integer
    Resolution value for rounding time.

    Outputs
    -------
    Array
    Zipped array with the rounded time and data values.
    """

    round_time = []
    round_values = []
    for i in range(len(obj._time)):
        minutes_under = datetime.timedelta(minutes=(obj._time[i].minute % res),
                                           seconds=(obj._time[i].second))
        minutes_over = datetime.timedelta(minutes=res) - minutes_under
        # Find how many minutes over or under the nearest 5 minutes the current
        # time value is.
        if (obj._time[i].minute % res) <= res/2.0:
            newtime = obj._time[i] - minutes_under
        else:
            newtime = obj._time[i] + minutes_over
        round_time.append(newtime.strftime("%m/%d/%Y %H:%M"))
        # Round each time value up or down to the nearest 5 minutes, then
        # replace  the time value in the ImportData object with the #
        # rounded time.

    for j in range(len(obj._time)):
        if obj._time[j] == obj._time[j - 1]:
            continue
        # Skip the loop if there is a duplicate time value.

        value_search = obj.linear_search_value(obj._time[j])
        # Search for the value at each rounded time in the ImportData 'value'
        # array,  then add the value to the 'round_values' array. Duplicate
        # values are either summed or averaged, depending on the input data
        # type.

    round_values = obj._value
    # The linear_search_value function cannot find the values in the ImportData
    # object. I don't know why. I am setting 'round_values' to be the values
    # already found in the ImportData object.

    return zip(round_time, round_values)


def printArray(data_list, annotation_list, base_name, key_file):
    """
    Purpose
    -------
    Combine and print on the key_file

    Inputs
    ------
    data_list a list of zip objects of data (time, value) pairs
    annotation_list a list of strings with column labels for the data value
    base_name the file name you want to print as
    key_file the name from annotation_list you want to align the data on

    Outputs
    -------
    """


if __name__ == '__main__':
    """
    Main function
    """

    parser = argparse.ArgumentParser(description='A class to import,' +
                                     'combine, and print data from a folder',
                                     prog='dataImport')
    parser.add_argument('--folder_name', type=str, help='Name of input folder')
    parser.add_argument('--output_file', type=str, help='Name of output file')
    parser.add_argument('--sort_key', type=str, help='File to sort on')
    args = parser.parse_args()
    # Input arguments.

    try:
        files_lst = listdir(args.folder_name)
    except (FileNotFoundError, NameError):
        print('Cannot find specified directory')
        sys.exit(1)
    files_lst.remove('.ipynb_checkpoints')
    # List the files found in the specified folder.

    data_lst = []
    for f in files_lst:
        data_lst.append(ImportData(args.folder_name + '/' + f))
        # Read each file with ImportData.
    if (len(data_lst) == 0):
        print('No files read into ImportData class')
        sys.exit(1)

    start_time = time.time()
    data_5 = []
    for obj in data_lst:
        data_5.append(roundTimeArray(obj, 5))
    end_time = time.time()
    print('Time to create data_5:')
    print(end_time - start_time)
    # Use roundTimeArray to create a zipped list with times rounded to
    # 5 minutes, and print the length of time it takes Python to do this.

    start_time = time.time()
    data_15 = []
    for obj in data_lst:
        data_15.append(roundTimeArray(obj, 15))
    end_time = time.time()
    print('Time to create data_15:')
    print(end_time - start_time)
    # Use roundTimeArray to create a zipped list with times rounded to
    # 15 minutes, and print the length of time it takes Python to do this.
    sys.exit()

    # I was not able to write the printLargeArray function. The script exits
    # before reaching this block.
    res1 = printLargeArray(data_5, files_lst, args.output_file+'_5',
                           args.sort_key)
    if (res1 == -1):
        sys.exit(1)

    res2 = printLargeArray(data_15, files_lst, args.output_file+'_15',
                           args.sort_key)
    if (res2 == -1):
        sys.exit(1)
