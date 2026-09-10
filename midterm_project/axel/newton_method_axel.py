# Finding a root using Newton-Raphson
# Function:   y = x^3 - 5x - 1
# Derivative: dy = 3x^2 - 5
#
# Good test starting point: 3.0
# The root should be around 2.3301

def get_y(x):
    return (x ** 3) - (5 * x) - 1

def get_slope(x):
    return (3 * (x ** 2)) - 5

def find_zero(start_x, accuracy):
    current_x = start_x

    # Run up to 25 attempts
    for step in range(1, 26):
        y_val = get_y(current_x)
        slope_val = get_slope(current_x)

        # Print current progress
        print("Iteration", step, ": x =", round(current_x, 5), "| f(x) =", round(y_val, 5))

        # Check if we are close enough to zero
        if abs(y_val) < accuracy:
            print("Found root within accuracy!")
            return current_x

        # Can't divide by zero
        if slope_val == 0:
            print("Slope is zero! Cannot continue.")
            return None

        # Newton step
        next_x = current_x - (y_val / slope_val)

        # Move to next x
        current_x = next_x

    print("Hit max attempts without finishing.")
    return current_x


# User test input
print("Newton's Method for: x^3 - 5x - 1 = 0")
guess = float(input("Enter starting number (try 3.0): "))
target_error = 0.0001

final_root = find_zero(guess, target_error)

if final_root is not None:
    print("\nResult:")
    print("Root =", round(final_root, 4))
    print("Check f(root) =", round(get_y(final_root), 6))