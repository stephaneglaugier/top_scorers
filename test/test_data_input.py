import os
import tempfile
import unittest

from top_scorers.data_input import read_plain_text


class TestReadPlainText(unittest.TestCase):

    def test_read_valid_file(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(
                b'First Name,Second Name,Score\nDee,Moore,56\nSipho,Lolo,78\n')
            temp_file_name = temp_file.name

        content = read_plain_text(temp_file_name)
        os.unlink(temp_file_name)

        self.assertEqual(
            content, 'First Name,Second Name,Score\nDee,Moore,56\nSipho,Lolo,78\n')

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_plain_text("non_existent_file.txt")

    def test_empty_file(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file_name = temp_file.name

        content = read_plain_text(temp_file_name)
        os.unlink(temp_file_name)

        self.assertEqual(content, '')


if __name__ == '__main__':
    unittest.main()
