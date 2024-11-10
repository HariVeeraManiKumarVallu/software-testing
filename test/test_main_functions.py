import sys
import os

#add the src directory to the python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main_functions import count_words

def test_count_words():
    assert count_words("hello world") == 2
    assert count_words("this is a test") == 4
    assert count_words("") == 0
    assert count_words("  ") == 0 # test for whitespacing-only string
    