def swap(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

for i in range(1, n):
    j = i
    while j > 0 and a[j-1] > a[j]:
        swap(a, j-1, j)
        j -= 1

print(a)