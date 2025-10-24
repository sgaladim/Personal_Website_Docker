# test_basic.py - Basic test file in root directory
"""
Basic test file placed in the root directory to ensure pytest can find it.
This is a backup solution for CI/CD environments where test discovery might fail.
"""

def test_basic():
    """Basic test that always passes."""
    assert True

def test_math():
    """Simple math test."""
    assert 2 + 2 == 4

def test_string():
    """Simple string test."""
    assert "hello" in "hello world"
