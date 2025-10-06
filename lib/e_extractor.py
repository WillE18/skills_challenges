def e_extractor(string):
    e_letters = ''.join([letter for letter in string if letter == 'e'])
    non_e_letters = ''.join([letter for letter in string if letter != 'e'])
    return f'{e_letters}{non_e_letters}'