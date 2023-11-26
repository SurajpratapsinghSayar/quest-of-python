import unittest

from who_broke_my_cicd_pipeline_part1 import compare_versions


class TestCompareVersions(unittest.TestCase):
    def test_compare_versions(self):
        for line_a, line_b, expected in [
            (
                "Successfully installed foo-1.0 bar-baz-1.0.1 foo_baz-0.1",
                "Successfully installed foo-1.0 bar-baz-1.0.1 foo_baz-0.1",
                {},
            ),
            (
                "Successfully installed foo-1.0 bar-baz-1.0.1 foo_baz-0.1",
                "Successfully installed foo-1.1 bar-baz-1.0.1 foo_baz-0.1",
                {"foo": ["1.0", "1.1"]},
            ),
            (
                "Successfully installed foo-1.0 bar-baz-1.0.1 foo_baz-0.1",
                "Successfully installed foo-1.1 bar-baz-1.0.1 foo_baz-0.3",
                {"foo": ["1.0", "1.1"], "foo_baz": ["0.1", "0.3"]},
            ),
        ]:
            with self.subTest(line_a=line_a, line_b=line_b, expected=expected):
                actual = compare_versions(line_a, line_b)
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
