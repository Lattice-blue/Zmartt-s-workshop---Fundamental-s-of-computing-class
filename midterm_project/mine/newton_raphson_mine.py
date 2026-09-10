# First principles:
# 1. We don't have a bracket [a, b] anymore. We start with a single guess (x0).
# 2. We use the slope (derivative) of the curve at that point to draw a straight tangent line.
# 3. Tangent line formula from algebra: y - y0 = m * (x - x0)
#    Here: y0 = f(x0), and slope m = df(x0).
# 4. We want to find where that straight line hits the horizontal axis (where y = 0).
#    0 - f(x0) = df(x0) * (x1 - x0)
#    -f(x0) / df(x0) = x1 - x0
#    x1 = x0 - (f(x0) / df(x0))
# 5. This formula projects our next better guess: x_next = x - f(x) / df(x)

# Edge case / Trap:
# What if the curve is completely flat at our guess? (df(x) == 0)
# A horizontal line never hits the horizontal axis (division by zero). We must fail fast.

# I believe I can eventually become highly competent in this


def newton_raphson(f, df, x0, tolerance, max_iter=100):
    # Start at our initial guess
    x = x0

    iteration = 0
    print(
        f"{'Iter':<6} | {'x_current':<12} | {'f(x)':<14} | {'f_prime(x)':<14} | {'x_next':<12}"
    )
    print("-" * 68)

    # Keep refining while the height (output) is further from zero than our acceptable range
    while abs(f(x)) > tolerance:
        # Prevent infinite loops if the algorithm gets thrown off into infinity
        if iteration >= max_iter:
            raise RuntimeError(
                f"Did not converge after {max_iter} iterations. Pick a better initial guess."
            )

        # Fail-fast: check if the tangent line is completely flat (slope is zero)
        slope = df(x)
        if slope == 0:
            raise ZeroDivisionError(
                "Slope f'(x) is zero! Tangent line is parallel to the x-axis and will never intersect."
            )

        # Apply the Newton-Raphson formula
        x_next = x - (f(x) / slope)

        iteration += 1
        print(
            f"{iteration:<6} | {x:<12.6f} | {f(x):<14.6e} | {slope:<14.6e} | {x_next:<12.6f}"
        )

        # Step forward to the new coordinate
        x = x_next

    # Once within tolerance, return the input coordinate that hits zero height
    return x


# DEFINE the function and its slope machine (derivative) here
# Power rule: x^3 -> 3*x^2, -x -> -1, -2 -> 0


def func(x):
    return x**3 - x - 2


def dfunc(x):
    return 3 * (x**2) - 1


# ASKS for a single initial starting guess
# NOTE: Use Desmos to pick an x value somewhat near where it crosses the horizontal line
print("Newton-Raphson Method for f(x) = x^3 - x - 2")
x0 = float(input("Enter initial guess (x0): "))

# HARD CODED in the tolerance value
TOLERANCE = 1e-6

# RUNS the Newton-Raphson algorithm
root = newton_raphson(func, dfunc, x0, TOLERANCE)

# PRINTS the root
print("-" * 68)
print(f"The root is: {root:.8f}")
print(f"Verification: f({root:.8f}) = {func(root):.6e}")