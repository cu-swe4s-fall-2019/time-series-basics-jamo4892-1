import unittest
import data_import
# Import modules.


class DataImportTest(unittest.TestCase):
    """
    This class contains unit tests that run on data_import.py
    The tests in the class instance are called in the main
    function below.
    """

    def test_importdata(self):
        file_name = './smallData/hr_small.csv'
        import_data_instance = data_import.ImportData(file_name)
        self.assertEqual(len(import_data_instance._time),
                         len(import_data_instance._value))
        # Assert that the length of the '_time' and '_value' arrays
        # from the ImportData class instance are the same.


if __name__ == '__main__':
    unittest.main()
