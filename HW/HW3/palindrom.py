my_str = input()
flag = True
for i in range(0, len(my_str)):
    if my_str[i] != my_str[len(my_str)-i-1]:
        flag = False
        break
print(f"Palindrom: {flag}")

