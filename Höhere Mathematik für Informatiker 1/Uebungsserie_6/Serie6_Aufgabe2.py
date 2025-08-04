import numpy as np


def muellti3_S6_Aufg2(A_matrix, b_vector):
    Mat_A = np.array(A_matrix, dtype=float)
    Vec_b = np.array(b_vector, dtype=float)
    n, m = Mat_A.shape

    if n != m:
        raise ValueError("Matrix A is not square")

    step_counter = 1
    for col_index in range(m - 1):
        if Mat_A[col_index, col_index] == 0:
            Mat_A, Vec_b = row_switch(Mat_A, Vec_b, col_index)

        for idx in range(n - step_counter):
            cur_row = n - idx - 1
            eliminate(Mat_A, Vec_b, cur_row, col_index)

        step_counter += 1

    U_mat = Mat_A
    det_of_A = calculate_determinant(U_mat)
    solution_vec = back_substitution(U_mat, Vec_b)
    return U_mat, det_of_A, solution_vec


def row_switch(matrix, vector, pivot_col):
    row_count = matrix.shape[0]
    for i in range(row_count - pivot_col - 1):
        target_row = row_count - i - 1
        if matrix[target_row, pivot_col] != 0:
            matrix[[pivot_col, target_row]] = matrix[[target_row, pivot_col]]
            vector[[pivot_col, target_row]] = vector[[target_row, pivot_col]]
    return matrix, vector


def eliminate(matrix_A, vector_b, cur_row, pivot_col):
    elim_factor = matrix_A[cur_row, pivot_col] / matrix_A[pivot_col, pivot_col]
    matrix_A[cur_row] -= elim_factor * matrix_A[pivot_col]
    vector_b[cur_row] -= elim_factor * vector_b[pivot_col]
    return matrix_A, vector_b


def calculate_determinant(U_matrix):
    det_val = 1.
    for i in range(U_matrix.shape[0]):
        det_val *= U_matrix[i, i]
    return det_val


def back_substitution(matrix_U, vector_b):
    num_rows = matrix_U.shape[0]
    sol_vector = np.zeros((num_rows, 1))
    for i in range(num_rows):
        current = num_rows - i - 1
        summation = sum(matrix_U[current, j] * sol_vector[j] for j in range(current + 1, num_rows))
        sol_vector[current] = (vector_b[current] - summation) / matrix_U[current, current]
    return sol_vector

'''
# Hauptprogramm von Aufgabe 1 a)
Mat_A = np.array([[20, 10, 0],
                  [50, 30, 20],
                  [200, 150, 100]])
Vec_b = np.array([[150],
                  [470],
                  [2150]])

print("Original Matrix A:")
print(Mat_A)
print("Original Vector b:")
print(Vec_b)

U, determinant, solution = muellti3_S6_Aufg2(Mat_A, Vec_b)

print("Upper triangle matrix U:")
print(U)
print("Solution vector:")
print(solution)
print("Determinant of A:")
print(determinant)
'''


# Hauptprogramm von Aufgabe 1 a)
Mat_A = np.array([[20000, 30000, 10000],
                  [10000, 17000, 6000],
                  [2000, 3000, 2000]])
Vec_b = np.array([[5200000],
                  [3000000],
                  [760000]])

print("Original Matrix A:")
print(Mat_A)
print("Original Vector b:")
print(Vec_b)

U, determinant, solution = muellti3_S6_Aufg2(Mat_A, Vec_b)

print("Upper triangle matrix U:")
print(U)
print("Solution vector:")
print(solution)
print("Determinant of A:")
print(determinant)
