# Bisection Method to find the root of an equation
# Function: f(x) = x^3 + x - 5
# Sample Interval to test:
# a = 1  --> f(1) = 1 + 1 - 5 = -3  (negative)
# b = 2  --> f(2) = 8 + 2 - 5 = 5   (positive)
# (Expected Root: around 1.516)

def f(x):
    return (x ** 3) + x - 5

def get_root_via_bisection(a, b, tolerance):
    # Check if endpoints are already the root
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b

    # Check if the signs are opposite
    if f(a) * f(b) > 0:
        print("Error: f(a) and f(b) must have opposite signs!")
        return None

    step = 0
    c = (a + b) / 2

    # Loop until f(c) is close enough to 0
    while abs(f(c)) > tolerance:
        step = step + 1
        print(f"Step {step}: a = {round(a, 4)}, b = {round(b, 4)}, mid = {round(c, 4)}, f(mid) = {round(f(c), 4)}")

        # Narrow down the interval
        if f(a) * f(c) > 0:
            a = c
        else:
            b = c

        c = (a + b) / 2

    return c

# --- User Inputs ---
print("Finding the root for: f(x) = x^3 + x - 5")
print("Suggested starting interval: a = 1, b = 2\n")

a = float(input("Enter start of interval (a): "))
b = float(input("Enter end of interval (b): "))

# Tolerance (how close to 0 we want to get)
tolerance = 0.0001

# Run method
root = get_root_via_bisection(a, b, tolerance)

if root is not None:
    print("\nThe approximate root is:", round(root, 4))