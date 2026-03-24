"""test the app.py file."""

import unittest
from pathlib import Path
from pyTask.app.app import get_urls_from_file, get_status_code

BASE_DIR = Path(__file__).parent
CSV_FILE = BASE_DIR / "test.csv"

class TestApp(unittest.TestCase):
    """test the app.py file."""
    
    def test_get_url_from_file(self):
        """test get_url_from_file function."""
        urls = get_urls_from_file(CSV_FILE)
        self.assertEqual(urls, ["http://www.google.com", "http://nonexistent.url.test", "http://www.github.com"])

    def test_get_status_code(self):
        """test get_status_code function."""
        status = get_status_code("http://www.google.com")
        self.assertEqual(status, 200)

    def test_get_status_code_nonexistent(self):
        """test get_status_code function with nonexistent url."""
        status = get_status_code("http://nonexistent.url.test")
        self.assertIsNone(status)

    def test_get_status_code_github(self):
        """test get_status_code function with github url."""
        status = get_status_code("http://www.github.com")
        self.assertEqual(status, 200)