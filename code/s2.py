import numpy as np
hx = np.array([['-', 1, 1, 1, 1, 1, 1],
                    [2, '-', 2, 2, 1, 1, 1],
                    [2, 1, '-', 1, 1, 1, 1],
                    [2, 1, 2, '-', 1, 1, 1],
                    [2, 2, 2, 2, '-', 1, 1],
                    [2, 2, 2, 2, 2, '-', 1],
                    [2, 2, 2, 2, 2, 2, '-']])
xj = np.array([['-', 1, 1, 1, 1, 1, 1],
                    [2, '-', 1, 1, 1, 1, 1],
                    [2, 2, '-', 1, 4, 1, 1],
                    [2, 2, 2, '-', 4, 1, 1],
                    [2, 2, 4, 4, '-', 1, 1],
                    [2, 2, 2, 2, 2, '-', 1],
                    [2, 2, 2, 2, 2, 2, '-']])
def calculate_difference_matrix(hx, xj):
    if hx.shape != xj.shape:
        raise ValueError("两个矩阵必须具有相同的形状")

    rows, cols = hx.shape
    difference_matrix = np.empty((rows, cols), dtype=object)

    for i in range(rows):
        for j in range(cols):
            if hx[i, j] == xj[i, j]:
                difference_matrix[i, j] = 0
            else:
                difference_matrix[i, j] = f"{hx[i, j]}/{xj[i, j]}"

    return difference_matrix

diff_matrix = calculate_difference_matrix(hx, xj)
print(diff_matrix)



