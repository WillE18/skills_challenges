import pytest
from lib.estimate_reading_time import *

def test_estimated_reading_time_empty_text():
    with pytest.raises(Exception) as e:
        estimate_reading_time('')
    error_message = str(e.value)
    assert error_message == 'Cannot estimate reading time for empty text.'

def test_estimated_reading_time_two_words():
    assert estimate_reading_time('Hello world') == 0.6

def test_estimated_reading_time_ten_words():
    assert estimate_reading_time('Hi, how are you? Had a good day so far?') == 3.0

def test_estimated_reading_time_twenty_five_words():
    assert estimate_reading_time('This is a pretty long sentence. This will definitely take a decent amount of time to read, in comparison to all the other ones atleast.') == 7.5

def test_estimated_reading_time_two_hundred_words():
    text = ' '.join(["word" for i in range(0,200)])
    assert estimate_reading_time(text) == 60.0

def test_estimated_reading_time_one_thousand_words():
    text = ' '.join(["word" for i in range(0,1000)])
    assert estimate_reading_time(text) == 300.0