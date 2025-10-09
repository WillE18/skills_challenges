import pytest
from lib.design_and_test_drive_complex_function import *

def test_wrong_format():
    with pytest.raises(Exception) as err:
        check_age('34')
    err_msg = str(err.value)
    assert err_msg == "Date must be in following format: YYYY-MM-DD"

def test_definitely_underage():
    result = check_age("2015-04-03")
    assert result == "Access denied: You are only 10, and need to be 16!"

def test_only_just_underage():
    result = check_age("2009-10-10") #as of 9/10/2025
    assert result == "Access denied: You are only 15, and need to be 16!"

def test_only_just_allowed_age():
    result = check_age("2009-10-09") #as of 9/10/2025
    assert result == "Access has been granted, you are old enough!"