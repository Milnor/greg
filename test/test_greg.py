import unittest

from greg import validated_arguments, string_from_file, main

class TestValidation(unittest.TestCase):

    def test_main(self):
        ''' Validate handling of command line arguments '''
        pass

    def test_string_from_file(self):
        self.assertRaises(TypeError, string_from_file, "job_description.docx")
        self.assertRaises(FileNotFoundError, string_from_file, "no_such_job_description.txt")

    def test_validated_arguments(self):
        pass

class TestResults(unittest.TestCase):

    def test_hidden_keywords(self):
        ''' Verify hidden text exists within output PDF '''
        pass

    def test_clean_output(self):
        ''' Verify modified PDF is visually equivalent to input PDF '''
        pass

if __name__ == "__main__":
    unittest.main()
