import unittest

from top_scorers.output import construct_output_str


class TestConstructOutputStr(unittest.TestCase):

    def test_single_name(self):
        names = ["Alice"]
        top_score = 10
        expected_output = "Alice\nScore: 10"
        self.assertEqual(construct_output_str(
            names, top_score), expected_output)

    def test_multiple_names(self):
        names = ["Alice", "Bob", "Charlie"]
        top_score = 20
        expected_output = "Alice\nBob\nCharlie\nScore: 20"
        self.assertEqual(construct_output_str(
            names, top_score), expected_output)

    def test_empty_names(self):
        names = []
        top_score = 0
        expected_output = "Score: 0"
        self.assertEqual(construct_output_str(
            names, top_score), expected_output)

    def test_non_zero_score_with_empty_names(self):
        names = []
        top_score = 5
        expected_output = "Score: 5"
        self.assertEqual(construct_output_str(
            names, top_score), expected_output)

    def test_negative_score(self):
        names = ["Alice", "Bob"]
        top_score = -5
        expected_output = "Alice\nBob\nScore: -5"
        self.assertEqual(construct_output_str(
            names, top_score), expected_output)


if __name__ == "__main__":
    unittest.main()
