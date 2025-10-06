def verify_sentence(text):
    if text.strip() == '':
        raise Exception('Cannot verify empty sentence.')
    sentence_finishers = ['.', '?', '!']
    if text[0].isupper() and text[-1] in sentence_finishers:
        return text
    if text[-1] in sentence_finishers:
        return text[0].upper()+text[1:]
    return text[0].upper()+text[1:]+'.'

""" misinterpreted actual challenge - just wanted a boolean response, rather than full correction
oh well, uses all the same principles, just slightly more complex than the actual challenge.
obviously logic is some what flawed in real world context - cant detect tonality of sentence
so always going to end with . as a pose to ever ending with ! or ? unless already supplied. """