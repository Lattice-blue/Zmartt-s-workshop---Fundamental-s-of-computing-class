# The function: f(x) = x^3 - x - 2
def f(x):
    return x**3 - x - 2


# The derivative (slope): f'(x) = 3x^2 - 1
def df(x):
    return 3 * (x**2) - 1


def newton_raphson(x0, tol):
    x = x0
    iteration = 0
    max_iter = 100

    # Print table header
    print("\nIter  | x_current    | f(x)         | f'(x)        | x_next")
    print("-" * 60)

    # Keep looping until f(x) is close enough to 0
    while abs(f(x)) > tol:
        iteration = iteration + 1

        # Stop if it takes too many steps
        if iteration > max_iter:
            print("Error: Could not find a root within 100 steps.")
            return None

        slope = df(x)

        # Avoid division by zero if the tangent line is flat
        if slope == 0:
            print("Error: Slope is zero! Tangent line is completely flat.")
            return None

        # Newton-Raphson formula: x_next = x - f(x) / f'(x)
        x_next = x - (f(x) / slope)

        print(
            f"{iteration:<5} | {x:<12.4f} | {f(x):<12.4f} | {slope:<12.4f} | {x_next:<12.4f}"
        )

        # Move to the next point
        x = x_next

    return x


# --- Main Program ---
print("Newton-Raphson Method for f(x) = x^3 - x - 2")
x0 = float(input("Enter initial guess (x0): "))
tolerance = 0.0001

root = newton_raphson(x0, tolerance)

if root is not None:
    print("-" * 60)
    print(f"The root is approximately: {root:.4f}")
    print(f"Check f(root): {f(root):.6f}")