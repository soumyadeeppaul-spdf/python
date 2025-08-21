
from lud1 import lu_decomposition_doolittle, multiply_matrices, read_matrix, print_matrix


A = read_matrix("C.txt")


L, U = lu_decomposition_doolittle(A)


print_matrix(A, "Matrix A (from C.txt)")
print("Using Doolittle’s Method for LU Decomposition\n")
print_matrix(L, "Lower Triangular Matrix L")
print_matrix(U, "Upper Triangular Matrix U")


A_check = multiply_matrices(L, U)
print_matrix(A_check, "Verification (L * U)")