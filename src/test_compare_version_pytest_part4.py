import pytest
from src.who_broke_my_cicd_pipeline_part1 import compare_versions


@pytest.mark.parametrize(
    "line_a, line_b, expected",
    [
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
    ],
)
def test_function(line_a, line_b, expected):
    assert compare_versions(line_a, line_b) == expected
