import numpy as np
from math import nan

def muellti3_S9_Aufg2(A_original, A_modified, b_original, b_modified):
    condition_number = np.linalg.cond(A_original, np.inf)

    diff_norm_A = np.linalg.norm((A_original - A_modified), np.inf)
    norm_A = np.linalg.norm(A_original, np.inf)
    diff_norm_b = np.linalg.norm((b_original - b_modified), np.inf)
    norm_b = np.linalg.norm(b_original, np.inf)

    solution_original = np.linalg.solve(A_original, b_original)
    solution_modified = np.linalg.solve(A_modified, b_modified)

    max_delta_x = (condition_number / (1 - (condition_number * (diff_norm_A / norm_A)))) * (
                (diff_norm_A / norm_A) + (diff_norm_b / norm_b))
    observed_delta_x = np.linalg.norm((solution_original - solution_modified), np.inf) / np.linalg.norm(
        solution_original, np.inf)

    if (condition_number * (diff_norm_A / norm_A)) >= 1:
        max_delta_x = nan

    return [solution_original, solution_modified, max_delta_x, observed_delta_x]


A = np.array([[20, 30, 10], [10, 17, 6], [2, 3, 2]])
A_modified = A - 0.1

b = np.array([[5720], [3300], [836]])
b_modified = b + 100

[solution_original, solution_modified, max_delta_x, observed_delta_x] = muellti3_S9_Aufg2(A, A_modified, b, b_modified)

print("Original-Lösung: ", solution_original)
print("Modifizierte Lösung mit Fehler: ", solution_modified)
print("Maximaler Delta x: ", max_delta_x)
print("Beobachteter Delta x: ", observed_delta_x)
