
def read_matrix(filename):
    matrix = []
    with open(filename, "r") as f:
        for line in f:
            row = []
            for num in line.strip().split():
                row.append(float(num))  # append values
            matrix.append(row)  # append row
    return matrix


def read_vector(filename):
    vector = []
    with open(filename, "r") as f:
        for line in f:
            for num in line.strip().split():
                vector.append(float(num))  # append elements
    return vector


# ---------- Symmetry Check ----------
def is_symmetric(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i][j] != A[j][i]:
                return False
    return True


# ---------- Cholesky decomposition ----------
def forward_substitution(L, b):
    n = len(b)
    y = [0.0] * n
    for i in range(n):
        s = 0.0
        for j in range(i):
            s += L[i][j] * y[j]
        y[i] = (b[i] - s) / L[i][i]
    return y


def backward_substitution(U, y):
    n = len(y)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = 0.0
        for j in range(i + 1, n):
            s += U[i][j] * x[j]
        x[i] = (y[i] - s) / U[i][i]
    return x


def cholesky_decomposition(A, b):
    # check symmetry
    if not is_symmetric(A):
        print("Error: Matrix is not symmetric. Cholesky decomposition not possible.")
        return None

    n = len(A)
    L = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1):
            s = 0.0
            for k in range(j):
                s += L[i][k] * L[j][k]

            if i == j:
                L[i][j] = (A[i][i] - s) ** 0.5
            else:
                L[i][j] = (A[i][j] - s) / L[j][j]

    # Solve Ly = b
    y = forward_substitution(L, b)

    # Transpose of L
    Lt = [[L[j][i] for j in range(n)] for i in range(n)]

    # Solve L^T x = y
    x = backward_substitution(Lt, y)
    return x


# ---------- Iterative methods ----------
def jacobi(A, b, tol=1e-6, max_iterations=1000):
    n = len(b)
    x = [0.0] * n
    x_new = [0.0] * n

    for iteration in range(max_iterations):
        for i in range(n):
            s = 0.0
            for j in range(n):
                if j != i:
                    s += A[i][j] * x[j]
            x_new[i] = (b[i] - s) / A[i][i]

        diff = max(abs(x_new[i] - x[i]) for i in range(n))
        if diff < tol:
            return x_new, iteration + 1
        x = x_new[:]

    return x, max_iterations


def gauss_seidel(A, b, tol=1e-6, max_iterations=1000):
    n = len(b)
    x = [0.0] * n

    for iteration in range(max_iterations):
        x_new = x[:]
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        diff = max(abs(x_new[i] - x[i]) for i in range(n))
        if diff < tol:
            return x_new, iteration + 1
        x = x_new[:]

    return x, max_iterations


# ---------- Rearrangement for diagonal dominance ----------
import itertools
def make_diagonally_dominant(A, b):
    n = len(A)


    indices = list(range(n))
    for perm in itertools.permutations(indices):
        A_new = [A[i][:] for i in perm]
        b_new = [b[i] for i in perm]

        ok = True
        for i in range(n):
            diag = abs(A_new[i][i])
            off_diag = sum(abs(A_new[i][j]) for j in range(n) if j != i)
            if diag < off_diag:
                ok = False
                break

        if ok:
            return A_new, b_new

    print("Warning: Could not make the matrix strictly diagonally dominant.")
    return A, b