# Function to solve: f(x) = x^3 - x - 2
def f(x):
    return x**3 - x - 2


def bisection(a, b, tol):
    # Step 1: Check if a root actually exists between a and b
    if f(a) * f(b) >= 0:
        print("Error: f(a) and f(b) must have opposite signs!")
        return None

    iteration = 0
    c = (a + b) / 2

    # Print the table header
    print("\nIter  | a          | b          | Midpoint (c) | f(c)")
    print("-" * 55)

    # Keep cutting the interval in half until we reach our tolerance
    while abs(f(c)) > tol:
        iteration = iteration + 1

        print(f"{iteration:<5} | {a:<10.4f} | {b:<10.4f} | {c:<12.4f} | {f(c):<10.4f}")

        # Decide which half of the interval to keep
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        # Find the new midpoint
        c = (a + b) / 2

        # Safeguard to prevent an infinite loop
        if iteration >= 100:
            print("Reached 100 iterations, stopping early.")
            break

    return c


# --- Main Program ---
print("Enter interval values for f(x) = x^3 - x - 2")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
tolerance = 0.0001

root = bisection(a, b, tolerance)

if root is not None:
    print("-" * 55)
    print(f"The root is approximately: {root:.4f}")