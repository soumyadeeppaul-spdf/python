#question --1
from gsjr import gauss_jordan, format_matrix

A = [
    [0, 2, 5],
    [3, -1, 2],
    [1, -1, 3]
]

b = [1, -2, 3]

solution, final_aug, steps = gauss_jordan(A, b)

for desc, mat in steps:
    print(f"\n--- {desc} ---")
    for row in format_matrix(mat):
        print(row)

print("\nFinal Augmented Matrix (Reduced Row Echelon Form):")
for row in format_matrix(final_aug):
    print(row)

print("\nSolution Vector (x, y, z):")
print(solution)





#question--2

from gsjr import gauss_jordan, format_matrix

# Coefficient matrix A
A = [
    [1, -1,  4, 0,  2,  9],   # eqn 1
    [0,  5, -2, 7,  8,  4],   # eqn 2
    [1,  0,  5, 7,  3, -2],   # eqn 3
    [6, -1,  2, 3,  0,  8],   # eqn 4
    [-4, 2,  0, 5, -5,  3],   # eqn 5
    [0,  7, -1, 5,  4, -2]    # eqn 6
]

# RHS vector b
b = [19, 2, 13, -7, -9, 2]

solution, final_aug, steps = gauss_jordan(A, b)
for desc, mat in steps:
    print(f"\n--- {desc} ---")
    for row in format_matrix(mat):
        print(row)

print("\nFinal Augmented Matrix (Reduced Row Echelon Form):")
for row in format_matrix(final_aug):
    print(row)

print("\nSolution Vector (a1 ... a6):")
print(solution)