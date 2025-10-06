from lib.count_words import *

def test_count_words_empty_string():
    assert count_words('') == 0

def test_count_words_1_word_string():
    assert count_words('book') == 1

def test_count_words_multiple_words():
    assert count_words('the cat sat on the mat.') == 6

def test_count_words_loads_of_words():
    assert count_words('Wow, would you look at the size of this sentence. That is a lot of words.') == 16