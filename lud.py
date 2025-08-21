#question--2

def lu_decomposition_doolittle(A):
    """
    LU decomposition using Doolittle's method (diag(L)=1).
    Input: A (list of lists), square n×n
    Output: L, U  (both n×n)
    """
    n = len(A)
    L = [[0.0 for _ in range(n)] for _ in range(n)]
    U = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        # Upper triangular U
        for k in range(i, n):
            sum_val = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - sum_val

        # Lower triangular L
        L[i][i] = 1.0
        for k in range(i + 1, n):
            sum_val = sum(L[k][j] * U[j][i] for j in range(i))
            if U[i][i] == 0:
                raise ZeroDivisionError("Zero pivot encountered; add pivoting if needed.")
            L[k][i] = (A[k][i] - sum_val) / U[i][i]

    return L, U


def forward_substitution(L, b):
    """Solve L y = b (L is unit-lower)."""
    n = len(L)
    y = [0.0 for _ in range(n)]
    for i in range(n):
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))
    return y


def backward_substitution(U, y):
    """Solve U x = y (U is upper-triangular)."""
    n = len(U)
    x = [0.0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        denom = U[i][i]
        if denom == 0:
            raise ZeroDivisionError("Zero pivot encountered in U.")
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / denom
    return x


def solve_lu(A, b):
    """Solve A x = b via LU (Doolittle) + forward/backward substitution."""
    L, U = lu_decomposition_doolittle(A)
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)
    return x, L, U


def multiply_matrices(A, B):
    """Matrix product (square n×n)."""
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def multiply_matrix_vector(A, x):
    """Matrix–vector product."""
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]


def read_matrix(filename):
    """Read a matrix from a whitespace-separated text file."""
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:  # skip empty lines
                continue
            row = [float(num) for num in line.split()]
            matrix.append(row)
    return matrix


def read_vector(filename):
    """Read a vector from a text file (one number per line OR space-separated)."""
    vals = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            vals.extend(float(num) for num in line.split())
    return vals


def print_matrix(M, name="Matrix"):
    print(f"{name}:")
    for row in M:
        print(["{:.6f}".format(v) for v in row])
    print()


def print_vector(v, name="Vector"):
    print(f"{name}: {[float(f'{val:.6f}') for val in v]}\n")

"""
question2: 
Matrix A (from file):
['1.000000', '-1.000000', '4.000000', '0.000000', '2.000000', '9.000000']
['0.000000', '5.000000', '-2.000000', '7.000000', '8.000000', '4.000000']
['1.000000', '0.000000', '5.000000', '7.000000', '3.000000', '-2.000000']
['6.000000', '-1.000000', '2.000000', '3.000000', '0.000000', '8.000000']
['-4.000000', '2.000000', '0.000000', '5.000000', '-5.000000', '3.000000']
['0.000000', '7.000000', '-1.000000', '5.000000', '4.000000', '-2.000000']

Vector b (from file): [19.0, 2.0, 13.0, -7.0, -9.0, 2.0]     

Lower Triangular L (Doolittle):
['1.000000', '0.000000', '0.000000', '0.000000', '0.000000', '0.000000']
['0.000000', '1.000000', '0.000000', '0.000000', '0.000000', '0.000000']
['1.000000', '0.200000', '1.000000', '0.000000', '0.000000', '0.000000']
['6.000000', '1.000000', '-14.285714', '1.000000', '0.000000', '0.000000']
['-4.000000', '-0.400000', '10.857143', '-0.697368', '1.000000', '0.000000']
['0.000000', '1.400000', '1.285714', '-0.157895', '1.517205', '1.000000']

Upper Triangular U:
['1.000000', '-1.000000', '4.000000', '0.000000', '2.000000', '9.000000']
['0.000000', '5.000000', '-2.000000', '7.000000', '8.000000', '4.000000']
['0.000000', '0.000000', '1.400000', '5.600000', '-0.600000', '-11.800000']
['0.000000', '0.000000', '0.000000', '76.000000', '-28.571429', '-218.571429']
['0.000000', '0.000000', '0.000000', '0.000000', '-7.210526', '16.289474']
['0.000000', '0.000000', '0.000000', '0.000000', '0.000000', '-51.654327']

Solution x (Ax = b): [-1.761817, 0.896228, 4.051931, -1.617131, 2.041914, 0.151832]

Verification (L * U ≈ A):
['1.000000', '-1.000000', '4.000000', '0.000000', '2.000000', '9.000000']
['0.000000', '5.000000', '-2.000000', '7.000000', '8.000000', '4.000000']
['1.000000', '0.000000', '5.000000', '7.000000', '3.000000', '-2.000000']
['6.000000', '-1.000000', '2.000000', '3.000000', '0.000000', '8.000000']
['-4.000000', '2.000000', '-0.000000', '5.000000', '-5.000000', '3.000000']
['0.000000', '7.000000', '-1.000000', '5.000000', '4.000000', '-2.000000']

Verification (A * x ≈ b): [19.0, 2.0, 13.0, -7.0, -9.0, 2.0] 

"""


#question --1
