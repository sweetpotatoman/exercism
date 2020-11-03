from re import findall
from collections import Counter


def count_words(sentence):
    word = findall(r"[a-zA-Z0-9]+'\w+|[a-zA-Z0-9]+", sentence.lower())
    return Counter(word)

print(count_words("First: don're laugh. Then: don're cry."))
print(count_words("''hey'' 1234 ''``hjf``f9010''"))
