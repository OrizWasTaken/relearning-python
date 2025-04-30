from pathlib import Path
import os

os.chdir('C:/Users/Oriz/Desktop/relearning python/exercises/chapter 10/exceptions')

def count_common_words(filename, word):
    """Count how many times word appears in the text."""
    # Note: This is a really simple approximation, and the number returned
    # will be higher than the actual count.
    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)

filename = 'alice.txt'
count_common_words(filename, 'the')