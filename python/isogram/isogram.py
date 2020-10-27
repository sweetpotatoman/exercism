def is_isogram(string):
    lower = string.lower()
    for x in lower:
        if x.isalpha() and lower.count(x) > 1:
            return False
    return True

# print(is_isogram('12-o-etw'))