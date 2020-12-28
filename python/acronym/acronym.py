import re

def abbreviate(words):
    if type(words) != str:
        raise ValueError("You have to type a string type word")
    words = re.sub(r'_|-', " ", words).split()
    one = ''
    for word in words:
        one += word[:1].upper()
    return one