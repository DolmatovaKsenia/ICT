summ = 0
flag = True
prev = 0
for i in range(10):
    number = int(input("Enter a number: "))
    if i == 0:
        prev = 0
    else:
        if prev > number:
            flag = False
    prev = number
    summ = summ + number
print(f"Sum: {summ}")
print(f"Increase: {flag}")


