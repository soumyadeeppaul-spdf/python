"""Soumyadeep Paul (2311182)"""
"""solving Assignment 4 on Cholesky and jacobi fractorization for linear equation solving"""

#question 1 ::

# Function to read a matrix from a text file
def read_matrix(filename):
    matrix = []
    with open(filename, "r") as f:
        for line in f:
            row = []
            for num in line.strip().split():
                row.append(float(num))  
            matrix.append(row)  
    return matrix


# Function to read a vector from a text file
def read_vector(filename):
    vector = []
    with open(filename, "r") as f:
        for line in f:
            for num in line.strip().split():
                vector.append(float(num))  
    return vector


# Forward substitution
def forward_substitution(L, b):
    n = len(b)
    y = [0.0] * n
    for i in range(n):
        s = 0.0
        for j in range(i):
            s += L[i][j] * y[j]
        y[i] = (b[i] - s) / L[i][i]
    return y


# Backward substitution
def backward_substitution(U, y):
    n = len(y)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = 0.0
        for j in range(i + 1, n):
            s += U[i][j] * x[j]
        x[i] = (y[i] - s) / U[i][i]
    return x


# Function for Cholesky decomposition
def cholesky_decomposition(A, b):
    n = len(A)
    # Initialize L
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

    # Solving Ly = b
    y = forward_substitution(L, b)

    # Transpose of L
    Lt = [[L[j][i] for j in range(n)] for i in range(n)]

    # Solving L^T x = y
    x = backward_substitution(Lt, y)
    return x


# question -2 :: Function for Jacobi Iterative Method

def jacobi_iteration(A, b, tol=1e-6, max_iterations=1000):
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

        # Convergence check (infinity norm)
        diff = max(abs(x_new[i] - x[i]) for i in range(n))
        if diff < tol:
            return x_new, iteration + 1

        x = x_new[:]

    return x, max_iterations



"""
ANSWER : 
Matrix A:
[[4.0, 1.0, 1.0, 1.0], [1.0, 3.0, -1.0, 1.0], [1.0, -1.0, 2.0, 0.0], [1.0, 1.0, 0.0, 2.0]]

Vector b:
[3.0, 3.0, 1.0, 3.0]

Solution using Cholesky decomposition:
[0.0, 1.0, 1.0, 1.0000000000000002]

Solution using Jacobi method:
[0.0, 0.9999994039535522, 0.9999997019767761, 0.9999997019767761]
Converged in 42 iterations
"""