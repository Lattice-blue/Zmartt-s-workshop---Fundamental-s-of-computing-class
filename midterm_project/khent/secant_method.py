# Secant Method root finder
# Equation: f(x) = x^3 - 6x - 4
#
# Starting points to test:
# Point 1: 2.0  ->  f(2.0) = -8.0
# Point 2: 3.0  ->  f(3.0) =  5.0
# Expected root is around 2.7321 (which is 1 + sqrt(3))

def target_eq(x):
    return (x ** 3) - (6 * x) - 4

def get_root(pt1, pt2, target_accuracy):
    # Try up to 30 steps
    for round_num in range(1, 31):
        y1 = target_eq(pt1)
        y2 = target_eq(pt2)

        # Calculate slope (rise over run)
        rise = y2 - y1
        run = pt2 - pt1

        # Check for a flat horizontal line
        if rise == 0:
            print("Slope is zero! Secant line is horizontal.")
            return None

        slope = rise / run

        # Find where this line hits the x-axis
        next_pt = pt2 - (y2 / slope)

        print("Step", round_num, ": current guess =", round(next_pt, 4), "| f(x) =", round(target_eq(next_pt), 5))

        # Check if we are close enough to zero
        if abs(target_eq(next_pt)) < target_accuracy:
            print("Found a close enough answer!")
            return next_pt

        # Shift coordinates forward for the next loop
        pt1 = pt2
        pt2 = next_pt

    print("Reached max steps without full accuracy.")
    return pt2


# User inputs
print("Finding root for: x^3 - 6x - 4 = 0")
val1 = float(input("Enter starting point 1 (try 2.0): "))
val2 = float(input("Enter starting point 2 (try 3.0): "))
accuracy = 0.0001

answer = get_root(val1, val2, accuracy)

if answer is not None:
    print("\nResult:")
    print("Found Root =", round(answer, 4))
    print("Check value at root =", round(target_eq(answer), 6))