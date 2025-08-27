import lib3

A = lib3.read_matrix("A3.txt")
b = lib3.read_vector("B3.txt")

print("Matrix A:")
print(A)
print("\nVector b:")
print(b)

# Solve using Cholesky
x_cholesky = lib3.cholesky_decomposition(A, b)
print("\nSolution using Cholesky decomposition:")
print(x_cholesky)

# Solve using Jacobi
x_jacobi, iterations = lib3.jacobi_iteration(A, b)
print("\nSolution using Jacobi method:")
print(x_jacobi)
print(f"Converged in {iterations} iterations")
