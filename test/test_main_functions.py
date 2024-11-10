# test/test_main_functions.py

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main_functions import count_words

def test_count_words():
    assert count_words("hello world") == 2
    assert count_words("this is a test") == 4
    assert count_words("") == 0
    assert count_words("   ") == 0  # Test for whitespace-only string