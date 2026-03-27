# Разложение вектора по ортогональному базису
import numpy as np

v = np.array(list(map(int, input().split())))

e1 = np.array(list(map(int, input().split())))
e2 = np.array(list(map(int, input().split())))
e3 = np.array(list(map(int, input().split())))

basis = np.array([e1, e2, e3])

c1 = np.dot(v, e1)
c2 = np.dot(v, e2)
c3 = np.dot(v, e3)
coeffs = np.array([c1, c2, c3])
print(coeffs)