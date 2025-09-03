import math

def f1(x):
    """Q1 function: f(x) = log(x/2) - sin(5x/2)"""
    return math.log(x/2) - math.sin(5*x/2)

def f2(x):
    """Q2 function: f(x) = -x - cos(x)"""
    return -x - math.cos(x)

# --- Bisection Method ---
def bisection(func, a, b, tol):
    print("\n--- Bisection Method ---")
    print("Iter\ta\tb\tmid\tf(mid)")

    if func(a) * func(b) >= 0:
        print("Bisection method fails. Wrong interval.")
        return None

    mid = a
    iteration = 1
    while (b - a) >= tol:
        mid = (a + b) / 2
        fm = func(mid)
        print(f"{iteration}\t{a:.6f}\t{b:.6f}\t{mid:.6f}\t{fm:.6f}")

        if fm == 0.0:
            break
        elif fm * func(a) < 0:
            b = mid
        else:
            a = mid
        iteration += 1

    print(f"Final Bisection Root ≈ {mid} (after {iteration} iterations)")
    return mid

# --- Regula Falsi Method ---
def regula_falsi(func, a, b, tol):
    print("\n--- Regula Falsi Method ---")
    print("Iter\ta\tb\tc\tf(c)")

    if func(a) * func(b) >= 0:
        print("Regula Falsi method fails. Wrong interval.")
        return None

    c = a
    iteration = 1
    while abs(func(c)) > tol:
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        fc = func(c)
        print(f"{iteration}\t{a:.6f}\t{b:.6f}\t{c:.6f}\t{fc:.6f}")

        if fc == 0:
            break
        elif fc * func(a) < 0:
            b = c
        else:
            a = c
        iteration += 1

    print(f"Final Regula Falsi Root ≈ {c} (after {iteration} iterations)")
    return c

# --- Interval finding for Q2 ---
def find_interval(func, a, b, step, max_range=10):
    print("\n--- Interval Finding ---")
    # First try the given interval
    x1, x2 = a, a + step
    while x2 <= b:
        if func(x1) * func(x2) < 0:
            print(f"Root lies in interval: [{x1}, {x2}]")
            return (x1, x2)
        x1, x2 = x2, x2 + step

    # If not found, expand search between -max_range and +max_range
    print(f"No root found in [{a}, {b}]. Expanding search...")
    x1 = -max_range
    x2 = x1 + step
    while x2 <= max_range:
        if func(x1) * func(x2) < 0:
            print(f"Root lies in interval: [{x1}, {x2}]")
            return (x1, x2)
        x1, x2 = x2, x2 + step

    print("No root found in the extended range.")
    return None