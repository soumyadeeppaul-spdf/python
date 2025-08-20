import matplotlib.pyplot as plt
import numpy as np

def plot_lcg_random_numbers(a=1103515245, c=12345, m=32768, seed=4.98, N=10000, k=5):
    """
    Parameters:
        a (int): LCG multiplier.
        c (int): LCG increment.
        m (int): LCG modulus.
        seed (float): Initial seed value.
        N (int): Number of points to generate.
        k (int): Lag for correlation plot.
    """
    
    x = np.zeros(N + k)
    x[0] = seed

    # LCG generation
    for i in range(N + k - 1):
        x[i+1] = (a * x[i] + c) % m

    # Normalize to [0, 1]
    x_norm = x / m

    # Prepare lagged data
    xi = x_norm[:N]
    xi_k = x_norm[k:k+N]

    # Scatter plot
    plt.figure(figsize=(6, 6))
    plt.scatter(xi, xi_k, s=5, alpha=0.6)
    plt.xlabel(r"$x_i$")
    plt.ylabel(fr"$x_{{i+{k}}}$")
    plt.title(f"LCG Random Numbers: k = {k}")
    plt.tight_layout()
    plt.show()

