# The function to solve: f(x) = x^3 - 2x + 2
# Note: No derivative function needed for the Secant Method!
def f(x):
    return x**3 - 2 * x + 2


def secant(x0, x1, tol):
    iteration = 0
    max_iter = 100

    # Print table header
    print("\nIter  | x0         | x1         | f(x1)        | x_next")
    print("-" * 55)

    # Keep looping until f(x1) is close enough to 0
    while abs(f(x1)) > tol:
        iteration = iteration + 1

        # Stop if it takes too many steps
        if iteration > max_iter:
            print("Error: Did not converge within 100 steps.")
            return None

        # Calculate difference in y (rise)
        delta_y = f(x1) - f(x0)

        # Avoid division by zero if both points have the same y-value (flat line)
        if delta_y == 0:
            print("Error: Division by zero! Secant line is horizontal.")
            return None

        # Secant formula
        x_next = x1 - (f(x1) * (x1 - x0)) / delta_y

        print(
            f"{iteration:<5} | {x0:<10.4f} | {x1:<10.4f} | {f(x1):<12.4f} | {x_next:<10.4f}"
        )

        # Shift values forward for the next round
        x0 = x1
        x1 = x_next

    return x1


# --- Main Program ---
print("Secant Method for f(x) = x^3 - 2*x + 2")
x0 = float(input("Enter first guess (x0):  "))
x1 = float(input("Enter second guess (x1): "))
tolerance = 0.0001

root = secant(x0, x1, tolerance)

if root is not None:
    print("-" * 55)
    print(f"The root is approximately: {root:.4f}")
    print(f"Check f(root): {f(root):.6f}")