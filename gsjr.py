"""SOUMYADEEP PAUL(2311182)"""

"""here i have tried to show all the steps till i get the answer,so that whenever i will go for theoriticaL understanding i can check all the steps clearly"""


def format_matrix(matrix):
    """Format matrix rows for printing."""
    return [" ".join("{:8.4f}".format(val) for val in row) for row in matrix]

def gauss_jordan(A, b):
    n = len(b)
    steps = []   
    
    aug = []
    for i in range(n):
        row = A[i][:]
        row.append(b[i])
        aug.append(row)

    steps.append(("Initial Augmented Matrix", [r[:] for r in aug]))

    for i in range(n):
        # Partial pivoting
        max_row = i
        for k in range(i+1, n):
            if abs(aug[k][i]) > abs(aug[max_row][i]):
                max_row = k
        if aug[max_row][i] == 0:
            raise ValueError("Matrix is singular!")
        if max_row != i:
            aug[i], aug[max_row] = aug[max_row], aug[i]
            steps.append((f"After Pivoting at column {i+1}", [r[:] for r in aug]))

        # Making pivot = 1
        pivot = aug[i][i]
        aug[i] = [x / pivot for x in aug[i]]
        steps.append((f"Normalize Pivot Row {i+1}", [r[:] for r in aug]))

        # Eliminating other rows
        for j in range(n):
            if j != i:
                factor = aug[j][i]
                aug[j] = [aug[j][m] - factor * aug[i][m] for m in range(n+1)]
        steps.append((f"Eliminate other rows using Row {i+1}", [r[:] for r in aug]))

    # Extracting solution
    x = [aug[i][-1] for i in range(n)]
    return x, aug, steps