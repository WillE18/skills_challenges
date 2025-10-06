def estimate_reading_time(text):
    if text == '':
        raise Exception('Cannot estimate reading time for empty text.')
    word_count = len(text.split())
    seconds_per_word = 60/200
    return word_count*seconds_per_word