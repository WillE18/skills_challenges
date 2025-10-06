import pytest
from lib.verify_sentence import *

def test_verify_sentence_empty():
    with pytest.raises(Exception) as e:
        verify_sentence('')
    error_message = str(e.value)
    assert error_message == 'Cannot verify empty sentence.'

def test_verify_sentence_already_valid():
    assert verify_sentence('Hello world.') == 'Hello world.'

def test_verify_sentence_needs_both_changes():
    assert verify_sentence('hello world') == 'Hello world.'

def test_verify_longer_sentence_needs_both_changes():
    assert verify_sentence('this is a bad sentence') == 'This is a bad sentence.'

def test_verify_sentence_with_grammar_no_capital():
    assert verify_sentence('this sentence is half okay.') == 'This sentence is half okay.'

def test_verify_sentence_with_capital_no_grammar():
    assert verify_sentence('This is also half right') == 'This is also half right.'

def test_verify_sentence_with_different_grammar():
    verify_sentence('Does this one work?') == 'Does this one work?' 

def test_verify_sentence_different_grammar_np_capital():
    assert verify_sentence('but what about this one!') == 'But what about this one!'

def test_verify_sentence_empty_space():
    with pytest.raises(Exception) as e:
        verify_sentence(' ')
    error_message = str(e.value)
    assert error_message == 'Cannot verify empty sentence.'