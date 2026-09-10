# Program to find a root using Newton's Method
# Equation: f(x) = x^3 - 2x - 5
# Derivative: f'(x) = 3x^2 - 2
#
# Good initial guess to try: 2
# Expected root is around 2.0946

# The main equation
def equation(x):
    return x**3 - 2*x - 5

# The derivative of the equation
def derivative(x):
    return 3 * (x**2) - 2

# Newton's method solver
def solve_newton(guess, tolerance):
    x = guess
    count = 0
    max_steps = 50

    # Keep looping while f(x) is not close enough to 0
    while abs(equation(x)) > tolerance:
        count = count + 1

        # Stop if taking too long
        if count > max_steps:
            print("Did not converge after", max_steps, "steps. Try a different guess.")
            return None

        slope = derivative(x)

        # Check for division by zero
        if slope == 0:
            print("Error: Slope is 0. Cannot divide by zero.")
            return None

        # Newton's formula: next_x = x - (f(x) / f'(x))
        next_x = x - (equation(x) / slope)

        print("Step", count, ": current x =", round(x, 4), "| next x =", round(next_x, 4))

        # Update x for the next round
        x = next_x

    return x


# Get user input
print("Newton's Method for f(x) = x^3 - 2x - 5")
start_guess = float(input("Enter starting guess (e.g., 2): "))
tol = 0.0001

# Calculate
answer = solve_newton(start_guess, tol)

# Show result
if answer is not None:
    print("\nThe approximate root is:", round(answer, 4))
    print("Checking f(root):", round(equation(answer), 6))