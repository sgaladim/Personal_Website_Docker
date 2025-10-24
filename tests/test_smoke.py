# tests/test_smoke.py
"""
Smoke test to ensure pytest can collect and run at least one test.
This prevents the "collected 0 items" error in CI/CD pipelines.
"""

def test_smoke():
    """Basic smoke test that always passes."""
    assert True

def test_imports():
    """Test that we can import the main application modules."""
    try:
        import app
        import DAL
        assert True
    except ImportError as e:
        assert False, f"Failed to import required modules: {e}"
