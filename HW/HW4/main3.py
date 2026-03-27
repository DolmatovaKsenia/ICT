# вектора из списка
import numpy as np

# vectors = [
#     np.array([1, 0]),
#     np.array([0, 1]),
#     np.array([1, 1]),
#     np.array([-1, 1]),
#     np.array([0, 0])
# ]
vectors = []
n = int(input())
for i in range(n):
    vectors.append(np.array(list(map(int, input().split()))))

orthogonal_pairs = []

for i in range(len(vectors)):
    for j in range(i + 1, len(vectors)):
        if np.dot(vectors[i], vectors[j]) == 0:
            orthogonal_pairs.append((vectors[i], vectors[j]))

print(f"Найдено пар: {len(orthogonal_pairs)}")
for pair in orthogonal_pairs:
    print(f"{pair[0]} и {pair[1]}")