# Проекция вектора на вектор
import numpy as np

vec_a = np.array(list(map(int, input().split())))
vec_b = np.array(list(map(int, input().split())))

proj = np.dot(vec_a, vec_b) / np.linalg.norm(vec_b)
print(proj)