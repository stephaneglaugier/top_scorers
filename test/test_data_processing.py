import unittest

from top_scorers.data_processing import (calculate_top_score, idxs_with_score,
                                         names_from_idxs, process_data)


class TestMainFunctions(unittest.TestCase):

    def test_calculate_top_score(self):
        data = [
            ['John', 'Doe', 90],
            ['Jane', 'Doe', 85],
            ['Sam', 'Smith', 92]
        ]
        self.assertEqual(calculate_top_score(data), 92)

    def test_idxs_with_score(self):
        data = [
            ['John', 'Doe', 90],
            ['Jane', 'Doe', 90],
            ['Sam', 'Smith', 92]
        ]
        self.assertEqual(idxs_with_score(data, 90), [0, 1])

    def test_names_from_idxs(self):
        data = [
            ['John', 'Doe', 90],
            ['Jane', 'Doe', 85],
            ['Sam', 'Smith', 92]
        ]
        self.assertEqual(names_from_idxs(data, [0, 2]), [
                         'John Doe', 'Sam Smith'])

    def test_process_data(self):
        data = [
            ['John', 'Doe', 90],
            ['Jane', 'Doe', 85],
            ['Sam', 'Smith', 92]
        ]
        self.assertEqual(process_data(data), (['Sam Smith'], 92))

    def test_sorted_names(self):
        data = [
            ['John', 'Doe', 90],
            ['Jane', 'Doe', 90],
            ['Sam', 'Smith', 90]
        ]
        self.assertEqual(process_data(data)[0], [
                         'Jane Doe', 'John Doe', 'Sam Smith'])


if __name__ == "__main__":
    unittest.main()
