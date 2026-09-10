# How tf am I supposed to make the Secant Method

# First principles:
# 1. Newton-Raphson is fast, but calculating derivatives (f'(x)) by hand sucks.
# 2. Secant Method skips calculus and uses middle-school algebra for the slope.
# 3. We take TWO initial points: (x0, f(x0)) and (x1, f(x1)).
# 4. Standard slope between two points (rise over run):
#    m = (f(x1) - f(x0)) / (x1 - x0)
# 5. Substitute this slope 'm' directly into Newton's formula:
#    x_next = x1 - (f(x1) / m)
#    x_next = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
# 6. We do NOT need a bracket with opposite signs! We just need two starting guesses.
# 7. For the next loop, the points slide forward:
#    x0 becomes the old x1
#    x1 becomes x_next

# Edge case / Trap:
# What if both points have the exact same output height? f(x1) == f(x0)
# Then f(x1) - f(x0) = 0 (division by zero). The secant line is flat horizontal.
# We must fail fast.

# I believe I can eventually become highly competent in this


def secant_method(f, x0, x1, tolerance, max_iter=100):
    # Fail-fast check if one of the starting guesses is already an exact root
    if f(x0) == 0:
        return x0
    if f(x1) == 0:
        return x1

    iteration = 0
    print(
        f"{'Iter':<6} | {'x0':<12} | {'x1':<12} | {'f(x1)':<14} | {'x_next':<12}"
    )
    print("-" * 68)

    # Keep looping while the current guess height is outside acceptable tolerance
    while abs(f(x1)) > tolerance:
        # Prevent runaway execution
        if iteration >= max_iter:
            raise RuntimeError(
                f"Did not converge after {max_iter} iterations. Try different starting points."
            )

        # Fail-fast: check if vertical difference is zero (horizontal line trap)
        delta_y = f(x1) - f(x0)
        if delta_y == 0:
            raise ZeroDivisionError(
                "f(x1) - f(x0) is zero! Secant line is horizontal and will never hit the axis."
            )

        # Apply Secant formula (finite-difference approximation of Newton-Raphson)
        x_next = x1 - (f(x1) * (x1 - x0)) / delta_y

        iteration += 1
        print(
            f"{iteration:<6} | {x0:<12.6f} | {x1:<12.6f} | {f(x1):<14.6e} | {x_next:<12.6f}"
        )

        # Slide the points forward for the next iteration
        x0 = x1
        x1 = x_next

    # Return the converged input coordinate
    return x1


# DEFINE the function here (Notice: NO DERIVATIVE FUNCTION NEEDED!)


def func(x):
    # return x**3 - x - 2
    # return 5 - x**3
    return x**3 - 2 * x + 2


# ASKS for two initial starting points
# NOTE: They don't need opposite signs, just two points near the crossing
print("Secant Method for f(x) = x^3 - 2*x + 2")
x0 = float(input("Enter initial guess x0: "))
x1 = float(input("Enter second guess x1: "))

# HARD CODED in the tolerance value
TOLERANCE = 1e-6

# RUNS the Secant algorithm
root = secant_method(func, x0, x1, TOLERANCE)

# PRINTS the root
print("-" * 68)
print(f"The root is: {root:.8f}")
print(f"Verification: f({root:.8f}) = {func(root):.6e}")