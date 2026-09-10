# Program to find the root of a function using the Bisection Method
# Equation: f(x) = x^3 - 4x - 9
#
# Sample test interval:
# a = 2  ->  f(2) = (2)^3 - 4(2) - 9 = -9  (negative)
# b = 3  ->  f(3) = (3)^3 - 4(3) - 9 = +6  (positive)
# Expected root is around 2.7065

def f(x):
    return x**3 - 4*x - 9

def bisection(a, b, tolerance):
    # Check if a root is already one of the endpoints
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b

    # Check if intermediate value theorem holds (must have opposite signs)
    if f(a) * f(b) > 0:
        print("Error: f(a) and f(b) must have opposite signs.")
        return None

    c = (a + b) / 2
    step = 1

    # Keep dividing the interval until f(c) is close enough to 0
    while abs(f(c)) > tolerance:
        print("Step", step, "-> Midpoint (c):", round(c, 5), "| f(c):", round(f(c), 5))

        # Check which half the root is in
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        c = (a + b) / 2
        step = step + 1

    return c

# User inputs
print("Bisection Method for f(x) = x^3 - 4x - 9")
a = float(input("Enter starting a: "))
b = float(input("Enter starting b: "))

tol = 0.0001

# Find the root
root = bisection(a, b, tol)

if root is not None:
    print("\nThe approximate root is:", round(root, 4))