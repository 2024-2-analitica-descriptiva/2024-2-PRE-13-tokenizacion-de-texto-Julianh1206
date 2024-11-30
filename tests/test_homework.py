"""Autograding script."""

import os


def test_homework():
    """Test homework."""
    assert os.path.exists("files/input/file1.txt")
    assert os.path.exists("files/input/file2.txt")
    assert os.path.exists("files/input/file3.txt")
