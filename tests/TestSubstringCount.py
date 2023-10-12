import unittest
from unittest.mock import patch
from io import StringIO
import os

# Import the function to be tested from the main program
from scramble import count_substrings

class TestSubstringCount(unittest.TestCase):
    def test_count_substrings(self):
        # Create a dictionary file with some words
        dictionary_data = "axpaj\napxaj\ndnrbt\npjxdn\nabd\n"
        with open("dictionary_new.txt", "w") as dict_file:
            dict_file.write(dictionary_data)

        # Create an input file with a test string
        input_data = "aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt\n"
        with open("input_new.txt", "w") as input_file:
            input_file.write(input_data)

        # Use patch to capture stdout
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Call the function to be tested
            count_substrings("dictionary_new.txt", "input_new.txt")

        # Check the program's output
        expected_output = "Case #1: 5\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
