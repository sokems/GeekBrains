"""Напишите функцию для транспонирования матрицы"""


def trans_matrix(matrix: list):
    new_matrix = []
    count = 0
    len_colunm = len(matrix)
    len_row = len(matrix[0])

    for _ in range(max(len_row, len_colunm)):
        inner_matrix = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j == count:
                    inner_matrix.append(matrix[i][j])
        new_matrix.append(inner_matrix)
        count += 1
    return new_matrix


matrix = [[1, 2, 3], [4, 5, 6]]

print(trans_matrix(matrix))