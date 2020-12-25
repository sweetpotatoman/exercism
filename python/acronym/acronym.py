def abbreviate(words):
    words = words.split()
    one = ''
    for word in words:
        one += word[:1].upper()
    return one

print(abbreviate("Portable Network Graphics"))
print(abbreviate("Portable _Network_ Graphics"))