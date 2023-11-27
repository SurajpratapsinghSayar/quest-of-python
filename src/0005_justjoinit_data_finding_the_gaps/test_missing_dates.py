import pathlib
import unittest
from datetime import date

from missing_dates import find_missing_dates

ANSWER = (
    "2022-06-05, "
    "2022-09-12, "
    "2022-10-03, "
    "2022-10-10, "
    "2022-10-14, "
    "2022-10-17, "
    "2022-10-22, "
    "2022-10-23, "
    "2022-10-25, "
    "2022-10-29, "
    "2022-11-06, "
    "2022-11-12, "
    "2022-11-13, "
    "2022-12-11, "
    "2022-12-18, "
    "2022-12-26, "
    "2023-02-04, "
    "2023-02-07, "
    "2023-02-08, "
    "2023-02-26, "
    "2023-03-11, "
    "2023-03-12, "
    "2023-03-27, "
    "2023-04-03, "
    "2023-04-12, "
    "2023-04-14, "
    "2023-04-17, "
    "2023-04-19, "
    "2023-04-20, "
    "2023-04-21, "
    "2023-04-22, "
    "2023-04-24"
)


class TestMissingDates(unittest.TestCase):
    def test_missing_dates(self):
        result = find_missing_dates(
            input_directory=pathlib.Path("justjoinit_data")
        )
        self.assertEqual(result, ANSWER)


if __name__ == '__main__':
    unittest.main()
