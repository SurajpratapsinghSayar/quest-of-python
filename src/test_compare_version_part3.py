import pytest

from src.who_broke_my_cicd_pipeline_part1 import compare_versions

def test_noChange():
    line_a = "Successfully installed foo-1.0 bar-baz-1.0.1 foo_baz-0.1"
    line_b = "Successfully installed foo-1.0 bar-baz-1.0.1 foo_baz-0.1"

    actual = compare_versions(line_a, line_b)
    expected = {}
    assert actual == expected

def test_singleChange():
    test_case_2_line_a = "Successfully installed foo-1.0 bar-baz-1.0.1 foo_baz-0.1"
    test_case_2_line_b = "Successfully installed foo-1.1 bar-baz-1.0.1 foo_baz-0.1"

    actual = compare_versions(test_case_2_line_a, test_case_2_line_b)
    expected = {"foo": ["1.0", "1.1"]}
    assert actual == expected

def test_multipleChange():
    test_case_2_line_a = "Successfully installed foo-1.0 bar-baz-1.0.1 foo_baz-0.1"
    test_case_2_line_b = "Successfully installed foo-1.1 bar-baz-1.0.1 foo_baz-0.3"

    acutal = compare_versions(test_case_2_line_a, test_case_2_line_b)
    expected = {"foo": ["1.0", "1.1"], "foo_baz": ["0.1", "0.3"]}
    assert acutal == expected