def string_cleaner(string):
    for c in [' ', '-']:
        if c in string:
            string = string.replace(c, '')
    return string.lower()


def is_isogram(string):
    i = 0
    clean_str = string_cleaner(string)  # we run string through our cleaner function
    for c in clean_str[i:]:
        i += 1 
        if c in clean_str[i:]:
            return False
            break
    return True
