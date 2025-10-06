def verify_sentence(text):
    if text.strip() == '':
        raise Exception('Cannot verify empty sentence.')
    sentence_finishers = ['.', '?', '!']
    if text[0].isupper() and text[-1] in sentence_finishers:
        return text
    if text[-1] in sentence_finishers:
        return text[0].upper()+text[1:]
    return text[0].upper()+text[1:]+'.'