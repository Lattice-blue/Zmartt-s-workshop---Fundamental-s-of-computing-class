# Solving an equation using the Secant Method
# Equation: f(x) = x^3 - 8x + 2
#
# Starting points to try:
# first  = 2.0  ->  f(2.0) = -6.0
# second = 3.0  ->  f(3.0) =  5.0
# Expected root is around 2.7052

def compute_y(x):
    return (x ** 3) - (8 * x) + 2

def approximate_root(first, second, limit_error):
    count = 0

    # Keep looping until the y-value is close enough to zero
    while abs(compute_y(second)) > limit_error:
        count = count + 1

        # Stop if it runs too many times
        if count > 50:
            print("Stopped: Did not find root within 50 tries.")
            return None

        y_first = compute_y(first)
        y_second = compute_y(second)

        # Difference in height (cannot divide by zero)
        y_difference = y_second - y_first
        if y_difference == 0:
            print("Error: Y-values are identical, cannot divide by zero.")
            return None

        # Secant formula
        next_val = second - (y_second * (second - first)) / y_difference

        print("Attempt", count, ": new guess =", round(next_val, 4), "| f(x) =", round(compute_y(next_val), 5))

        # Move the points forward
        first = second
        second = next_val

    return second


# User inputs
print("Finding root for: x^3 - 8x + 2 = 0")
p0 = float(input("Enter first start number (try 2.0): "))
p1 = float(input("Enter second start number (try 3.0): "))
tol = 0.0001

ans = approximate_root(p0, p1, tol)

if ans is not None:
    print("\nResult:")
    print("Estimated root =", round(ans, 4))
    print("Check compute_y(root) =", round(compute_y(ans), 6))