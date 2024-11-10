#main_functions.py

def count_words(text):
    """counts the number of words in a string."""
    if not text.strip():
        return 0
    return len(text.split())