"""soumyadeep pAUL(2311182)
QUESTION--1"""

def lu_decomposition_doolittle(A):
    """
    Performs LU Decomposition using Doolittle’s method (L has 1s on diagonal).
    Input: A (list of lists) - square matrix
    Output: (L, U)
    """
    n = len(A)
    L = [[0.0 for _ in range(n)] for _ in range(n)]
    U = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        # Upper Triangular
        for k in range(i, n):
            sum_val = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - sum_val

        # Lower Triangular
        L[i][i] = 1.0
        for k in range(i+1, n):
            sum_val = sum(L[k][j] * U[j][i] for j in range(i))
            L[k][i] = (A[k][i] - sum_val) / U[i][i]

    return L, U


def multiply_matrices(A, B):
    """Multiply two square matrices A and B."""
    n = len(A)
    result = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
    return result


def read_matrix(filename):
    """Read a matrix from a text file."""
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            row = [float(num) for num in line.strip().split()]
            matrix.append(row)
    return matrix


def print_matrix(M, name="Matrix"):
    """Pretty-print matrix."""
    print(f"{name}:")
    for row in M:
        print(["{:.2f}".format(val) for val in row])
    print()

    """
    answer--1:
    Matrix A (from C.txt):
['1.00', '2.00', '4.00']
['3.00', '8.00', '14.00']
['2.00', '6.00', '13.00']

Using Doolittle’s Method for LU Decomposition

Lower Triangular Matrix L:
['1.00', '0.00', '0.00']
['3.00', '1.00', '0.00']
['2.00', '1.00', '1.00']

Upper Triangular Matrix U:
['1.00', '2.00', '4.00']
['0.00', '2.00', '2.00']
['0.00', '0.00', '3.00']

Verification (L * U):
['1.00', '2.00', '4.00']
['3.00', '8.00', '14.00']
['2.00', '6.00', '13.00']
"""