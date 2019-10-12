import csv
import dateutil.parser
from os import listdir
from os.path import isfile, join
import argparse
import datetime
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

        with open(data_csv, "r") as fhandle:
            reader = csv.DictReader(fhandle)
            # Read the file into an array.
            for row in reader:
                try:
                    self._time.append(dateutil.parser.parse(row['time']))
                    # Append each 'time' value in the 'reader' array to the
                    # '_time' array.
                except ValueError:
                    print("Input 'time' has bad format")
                    print(row['time'])
                    sys.exit(1)
                    # Find & print any 'time' value that gives a ValueError.
                self._value.append(row['value'])
                # Append each 'value' value in the 'reader' array to the
                # '_value' array.
            fhandle.close()

        #self.roundTime(5)
        # TBD.

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
                value.append(self_.value[i])
                # If the input key time is in the '_time' array,
                # append the _value value of the key to the 'value' array.

            if len(value) == 0:
                print('No values found for the selected key_time')
                return -1


def roundTimeArray(obj, res):
    """
    Purpose
    -------
    
    Inputs
    ------
    Obj:
    
    Res: Integer
    Resolution value for rounding time.
    
    Outputs
    -------
    
    """
    
    # Inputs: obj (ImportData Object) and res (rounding resoultion)
    # objective:
    # create a list of datetime entries and associated values with the times rounded to the nearest rounding resolution (res)
    # ensure no duplicated times
    # handle duplicated values for a single timestamp based on instructions in the assignment
    # return: iterable zip object of the two lists
    # note: you can create additional variables to help with this task which are not returned


def printArray(data_list, annotation_list, base_name, key_file):
    # combine and print on the key_file

if __name__ == '__main__':

    #adding arguments
    parser = argparse.ArgumentParser(description= 'A class to import, combine, and print data from a folder.',
    prog= 'dataImport')

    parser.add_argument('folder_name', type = str, help = 'Name of the folder')

    parser.add_argument('output_file', type=str, help = 'Name of Output file')

    parser.add_argument('sort_key', type = str, help = 'File to sort on')

    parser.add_argument('--number_of_files', type = int,
                        help = "Number of Files", required = False)

    args = parser.parse_args()


    #pull all the folders in the file
    files_lst = # list the folders


    #import all the files into a list of ImportData objects (in a loop!)
    data_lst = []

    #create two new lists of zip objects
    # do this in a loop, where you loop through the data_lst
    data_5 = [] # a list with time rounded to 5min
    data_15 = [] # a list with time rounded to 15min

    #print to a csv file
    printLargeArray(data_5,files_lst,args.output_file+'_5',args.sort_key)
    printLargeArray(data_15, files_lst,args.output_file+'_15',args.sort_key)
