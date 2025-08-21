# main.py
from lud import lu_decomposition_doolittle, multiply_matrices, solve_lu
from lud import read_matrix, read_vector, print_matrix, print_vector
import os

# --- Step 1: Read A from file ---
A = read_matrix("A.txt")

# --- Step 2: Check if b.txt exists (system solving case) ---
if os.path.exists("b.txt"):
    b = read_vector("b.txt")

    # Solve Ax = b using LU
    x, L, U = solve_lu(A, b)

    # Print results
    print_matrix(A, "Matrix A (from file)")
    print_vector(b, "Vector b (from file)")
    print_matrix(L, "Lower Triangular L (Doolittle)")
    print_matrix(U, "Upper Triangular U")
    print_vector(x, "Solution x (Ax = b)")

    # Verification
    Ax = multiply_matrices(L, U)   # Reconstruct A
    print_matrix(Ax, "Verification (L * U ≈ A)")

    b_check = [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]
    print_vector(b_check, "Verification (A * x ≈ b)")

else:
    # Just decomposition and verification
    L, U = lu_decomposition_doolittle(A)

    print_matrix(A, "Matrix A (from file)")
    print_matrix(L, "Lower Triangular L (Doolittle)")
    print_matrix(U, "Upper Triangular U")

    # Verification
    A_check = multiply_matrices(L, U)
    print_matrix(A_check, "Verification (L * U ≈ A)")