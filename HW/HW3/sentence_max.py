sentence = input()
words = sentence.split(" ")
print(words)
max_len = 0
max_word = ""
for word in words:
    cur_len = len(word)
    if cur_len > max_len:
        max_word = word
print(max_word)