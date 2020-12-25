# exercism


### review
- matrix
```
def column(self, index):
    # print(self.data)
    return([x[index-1] for x in self.data])
```

- word-count
```
def count_words(sentence):
    word = findall(r"[a-zA-Z0-9]+'\w+|[a-zA-Z0-9]+", sentence.lower())
    return Counter(word)
```