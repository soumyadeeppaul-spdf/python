
"""Soumyadeep Paul(2311182)"""


import lib4
# ---------- Question 1 ----------
A = lib4.read_matrix("A4.txt")
b = lib4.read_vector("B4.txt")

print("Question 1:")
print("Matrix A =")
for row in A:
    print(row)
print("Vector b =", b)

# Cholesky
x_cholesky = lib4.cholesky_decomposition(A, b)
if x_cholesky is not None:
    print("\nSolution using Cholesky decomposition:")
    print(x_cholesky)

# Gauss-Seidel
x_gs, it_gs = lib4.gauss_seidel(A, b)
print("\nSolution using Gauss-Seidel:")
print(x_gs, "in", it_gs, "iterations")


# ---------- Question 2 ----------
C = lib4.read_matrix("C4.txt")
d = lib4.read_vector("D4.txt")

print("\nQuestion 2:")
print("Original Matrix C =")
for row in C:
    print(row)
print("Original Vector d =", d)

# Rearrange for diagonal dominance
C, d = lib4.make_diagonally_dominant(C, d)

print("\nRearranged Matrix C =")
for row in C:
    print(row)
print("Rearranged Vector d =", d)

# Jacobi
x_jac, it_jac = lib4.jacobi(C, d)
print("\nSolution using Jacobi:")
print(x_jac, "in", it_jac, "iterations")

# Gauss-Seidel
x_gs2, it_gs2 = lib4.gauss_seidel(C, d)
print("\nSolution using Gauss-Seidel:")
print(x_gs2, "in", it_gs2, "iterations")





"""
Question 1:
Matrix A =
[4.0, -1.0, 0.0, -1.0, 0.0, 0.0]
[-1.0, 4.0, -1.0, 0.0, -1.0, 0.0]
[0.0, -1.0, 4.0, 0.0, 0.0, -1.0]
[-1.0, 0.0, 0.0, 4.0, -1.0, 0.0]
[0.0, -1.0, 0.0, -1.0, 4.0, -1.0]
[0.0, 0.0, -1.0, 0.0, -1.0, 4.0]
Vector b = [2.0, 1.0, 2.0, 2.0, 1.0, 2.0]

Solution using Cholesky decomposition:
[1.0, 0.9999999999999999, 1.0, 1.0, 1.0, 1.0]

Solution using Gauss-Seidel:
[0.9999997530614102, 0.9999997892247294, 0.9999999100460266, 0.9999998509593769, 0.9999998727858708, 0.9999999457079743] in 16 iterations


Question 2:
Original Matrix C =
[4.0, 0.0, 4.0, 10.0, 1.0]
[0.0, 4.0, 2.0, 0.0, 1.0]
[2.0, 5.0, 1.0, 3.0, 13.0]
[11.0, 3.0, 0.0, 1.0, 2.0]
[3.0, 2.0, 7.0, 1.0, 0.0]
Original Vector d = [20.0, 15.0, 92.0, 51.0, 15.0]

Rearranged Matrix C =
[11.0, 3.0, 0.0, 1.0, 2.0]
[0.0, 4.0, 2.0, 0.0, 1.0]
[3.0, 2.0, 7.0, 1.0, 0.0]
[4.0, 0.0, 4.0, 10.0, 1.0]
[2.0, 5.0, 1.0, 3.0, 13.0]
Rearranged Vector d = [51.0, 15.0, 15.0, 20.0, 92.0]

Solution using Jacobi:
[2.9791649583226008, 2.215599258220273, 0.21128373337161171, 0.15231661140963978, 5.71503326456748] in 58 iterations

Solution using Gauss-Seidel:
[2.979165086347139, 2.215599676186742, 0.21128402698819157, 0.15231700827754802, 5.715033568811629] in 12 iterations

"""