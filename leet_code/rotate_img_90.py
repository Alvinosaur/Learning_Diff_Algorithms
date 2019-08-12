def using_extra_array(matrix):
    # Idea is that the ith row turns into the N-1-ith column
    # ex: zeroth row rotates right to become (N-1)th column
    rows, cols = len(matrix), len(matrix[0])
    new_mat = [[0]*rows for c in range(cols)]
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            new_mat[c][rows-r-1] = matrix[r][c]
    return new_mat


def in_place(matrix):
    N = len(matrix)
    for r in range(N//2 + 1):
        for c in range(r, N//2 + 1):
            temp1 = matrix[r][c]
            matrix[r][c] = matrix[N-1-c][r]
            matrix[N-1-c][r] = matrix[N-1-r][N-1-c]
            matrix[N-1-r][N-1-c] = matrix[c][N-1-r]
            matrix[c][N-1-r] = temp1


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix: print(row)
print()

res = using_extra_array(matrix)
for row in res: print(row)
print()

in_place(matrix)
for row in matrix: print(row)
print()
