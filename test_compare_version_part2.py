import unittest

from who_broke_my_cicd_pipeline_part1 import compare_versions


class TestCompareVersions(unittest.TestCase):
    def test_noChange(self):
        line_a = "Successfully installed foo-1.0 bar-baz-1.0.1 foo_baz-0.1"
        line_b = "Successfully installed foo-1.0 bar-baz-1.0.1 foo_baz-0.1"

        actual = compare_versions(line_a, line_b)
        excepted = {}
        self.assertEqual(actual, excepted)

    def test_singleChange(self):
        test_case_2_line_a = "Successfully installed foo-1.0 bar-baz-1.0.1 foo_baz-0.1"
        test_case_2_line_b = "Successfully installed foo-1.1 bar-baz-1.0.1 foo_baz-0.1"

        actual = compare_versions(test_case_2_line_a, test_case_2_line_b)
        expected = {"foo": ["1.0", "1.1"]}
        self.assertEqual(actual, expected)

    def test_multipleChange(self):
        test_case_2_line_a = "Successfully installed foo-1.0 bar-baz-1.0.1 foo_baz-0.1"
        test_case_2_line_b = "Successfully installed foo-1.1 bar-baz-1.0.1 foo_baz-0.3"

        acutal = compare_versions(test_case_2_line_a, test_case_2_line_b)
        expected = {"foo": ["1.0", "1.1"], "foo_baz": ["0.1", "0.3"]}
        self.assertEqual(acutal, expected)


if __name__ == "__main__":
    unittest.main()
