from lib.make_snippet import *

def test_make_snippet_more_than_five():
    assert make_snippet('The ginger cat ran away from home.') == 'The ginger cat ran away...'

def test_make_snippet_length_five():
    assert make_snippet('There was a ginger cat.') == 'There was a ginger cat.'

def test_make_snippet_less_than_five():
    assert make_snippet('The ginger cat.') == 'The ginger cat.'

def test_make_snippet_very_long():
    assert make_snippet('There was a ginger cat who ran away from home yesterday.') == 'There was a ginger cat...'

def test_given_empty_string():
    assert make_snippet('') == ''