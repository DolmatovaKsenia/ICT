glasnaya = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
soglasnaya = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ь"]

cnt_glasnaya = 0
cnt_soglasnaya = 0
word = input()
for w in word:
    if w in glasnaya:
        cnt_glasnaya += 1
    elif w in soglasnaya:
        cnt_soglasnaya += 1
print(f"Glasnaya: {cnt_glasnaya}")
print(f"Soglasnaya: {cnt_soglasnaya}")
