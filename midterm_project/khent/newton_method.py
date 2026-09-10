# Newton-Raphson approximation
# Equation:   x^3 - 7x + 3 = 0
# Derivative: 3x^2 - 7
#
# Starting guess to test: 3.0
# The root should be around 2.3714

# Main equation
def my_eq(x):
    return x**3 - 7*x + 3

# Derivative equation
def my_eq_prime(x):
    return 3 * (x**2) - 7

def estimate_root(start_val):
    x_old = start_val
    diff = 1.0   # Placeholder value to get the while loop started
    tries = 0

    # Keep going until the step size (difference) gets tiny
    while diff > 0.0001:
        tries = tries + 1
        
        # Stop after 20 attempts so it doesn't run forever
        if tries > 20:
            print("Took too many steps!")
            break

        top = my_eq(x_old)
        bottom = my_eq_prime(x_old)

        # Check for zero slope
        if bottom == 0:
            print("Cannot divide by a slope of zero.")
            return None

        # Calculate the new point
        x_new = x_old - (top / bottom)
        
        # Measure how much the guess moved
        diff = abs(x_new - x_old)

        print("Round", tries, ": guess =", round(x_new, 4), "| change =", round(diff, 5))

        # Set up for the next loop
        x_old = x_new

    return x_old


# Ask user for a starting guess
print("Finding root for: x^3 - 7x + 3 = 0")
user_guess = float(input("Enter starting guess (try 3.0): "))

answer = estimate_root(user_guess)

if answer is not None:
    print("\nAnswer found:")
    print("x =", round(answer, 4))
    print("Checking f(x) =", round(my_eq(answer), 5))