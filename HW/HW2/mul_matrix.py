def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
result = multiply_matrices(matrix1, matrix2)
print(result)