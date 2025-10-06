from lib.e_extractor import *

def test_empty_string():
    assert e_extractor('') == ''

def test_string_with_no_e():
    assert e_extractor('king') == 'king'

def test_one_e_extracts():
    assert e_extractor('hello') == 'ehllo'

def test_multiple_e_extracts():
    assert e_extractor('severance') == 'eeesvranc'

def test_loads_of_e_extracts():
    assert e_extractor('eeeeeeeeewoweeeeee') == 'eeeeeeeeeeeeeeewow'

def test_e_already_at_start():
    assert e_extractor('eeehllo') == 'eeehllo'

def test_only_e():
    assert e_extractor('eeeeeeeeee') == 'eeeeeeeeee'