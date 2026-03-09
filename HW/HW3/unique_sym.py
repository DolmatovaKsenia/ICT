text = "мама мыла раму мама"
sett = set()
words = text.split()
for word in words:
    for s in word:
        sett.add(s)
print(len(sett))
print(sett)