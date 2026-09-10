# Program to find a root using the Secant Method
# Equation: f(x) = x^3 - 4x + 1
#
# Starting guesses to try:
# x0 = 1.0  ->  f(1.0) = -2.0
# x1 = 2.0  ->  f(2.0) =  1.0
# Expected root is around 1.8608

# The equation we want to solve
def my_function(x):
    return (x ** 3) - (4 * x) + 1

# The secant method solver
def solve_secant(x0, x1, tolerance):
    # Check if either starting guess is already the root
    if my_function(x0) == 0:
        return x0
    if my_function(x1) == 0:
        return x1

    step = 0
    max_steps = 30

    # Keep looping until f(x1) is close enough to zero
    while abs(my_function(x1)) > tolerance:
        step = step + 1

        # Stop if taking too long
        if step > max_steps:
            print("Took too many steps! Root not found.")
            return None

        y0 = my_function(x0)
        y1 = my_function(x1)

        # Avoid dividing by zero if both outputs are the same
        if (y1 - y0) == 0:
            print("Error: Flat line (y1 - y0 = 0). Cannot divide by zero.")
            return None

        # Secant formula to find the next point
        x2 = x1 - (y1 * (x1 - x0)) / (y1 - y0)

        print("Step", step, ": guess =", round(x2, 5), "| f(x) =", round(my_function(x2), 5))

        # Slide points forward for the next round
        x0 = x1
        x1 = x2

    return x1


# Get starting values from user
print("Secant Method for f(x) = x^3 - 4x + 1")
guess0 = float(input("Enter first guess (try 1.0): "))
guess1 = float(input("Enter second guess (try 2.0): "))

target_tolerance = 0.0001

root = solve_secant(guess0, guess1, target_tolerance)

if root is not None:
    print("\nResult:")
    print("Approximate root =", round(root, 4))
    print("Check f(root) =", round(my_function(root), 6))