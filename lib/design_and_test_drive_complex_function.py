from datetime import datetime
from dateutil import relativedelta

def check_age(dob):
    if not format_is_valid(dob):
        raise Exception("Date must be in following format: YYYY-MM-DD")
    current_date = datetime.now().date()
    user_date = datetime.strptime(dob, '%Y-%m-%d').date()
    age = relativedelta.relativedelta(current_date, user_date).years
    if age < 16:
        return f"Access denied: You are only {age}, and need to be 16!"
    return "Access has been granted, you are old enough!"
    
def format_is_valid(dob):
    if not isinstance(dob, str):
        return False
    if not len(dob) == 10:
        return False
    if not dob[4] == '-' and not dob[7] == '-':
        return False
    if not dob.replace('-', '').isnumeric():
        return False
    return True
