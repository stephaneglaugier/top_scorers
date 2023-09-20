import unittest

from top_scorers.csv_parser import is_header, parse_csv


class TestCSVFunctions(unittest.TestCase):

    def test_is_header_true(self):
        self.assertTrue(is_header("First Name,Second Name,Score"))

    def test_is_header_false(self):
        self.assertFalse(is_header("Dee,Moore,56"))

    def test_parse_csv_valid_with_header(self):
        csv_string = """First Name,Second Name,Score
        Dee,Moore,56
        Sipho,Lolo,78
        Noosrat,Hoosain,64
        George,Of The Jungle,78"""
        expected_output = [
            ['Dee', 'Moore', 56],
            ['Sipho', 'Lolo', 78],
            ['Noosrat', 'Hoosain', 64],
            ['George', 'Of The Jungle', 78]
        ]
        self.assertEqual(parse_csv(csv_string), expected_output)

    def test_parse_csv_valid_without_header(self):
        csv_string = """Dee,Moore,56
        Sipho,Lolo,78"""
        expected_output = [
            ['Dee', 'Moore', 56],
            ['Sipho', 'Lolo', 78]
        ]
        self.assertEqual(parse_csv(csv_string), expected_output)

    def test_parse_csv_missing_fields(self):
        with self.assertRaises(ValueError):
            parse_csv("Dee,56")

    def test_parse_csv_non_integer_score(self):
        with self.assertRaises(ValueError):
            parse_csv("Dee,Moore,Fifty")

    def test_parse_csv_extra_fields(self):
        with self.assertRaises(ValueError):
            parse_csv("Dee,Moore,56,ExtraField")


if __name__ == '__main__':
    unittest.main()
