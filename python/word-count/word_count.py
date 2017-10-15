import re

def word_count(phrase):
    words = re.sub(r'[^a-zA-Z0-9]', ' ', phrase).lower().split(' ')
    s = set(words)
    s.discard('')
    result = {}
    for word in words:
        if word in result.keys():
            count = result[word]
        else:
            count = 0
        if word in s: 
            count += 1
            result[word] = count

    return result


