import unittest

from greg import string_from_file

class TestValidation(unittest.TestCase):

    def test_main(self):
        pass

    def test_string_from_file(self):
        self.assertRaises(TypeError, string_from_file, "job_description.docx")

if __name__ == "__main__":
    unittest.main()
