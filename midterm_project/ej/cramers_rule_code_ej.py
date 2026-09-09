def get_det(a, b, c, d):
    return (a * d) - (b * c)

def solve(a1, b1, c1, a2, b2, c2):
    D = get_det(a1, b1, a2, b2)
    Dx = get_det(c1, b1, c2, b2)
    Dy = get_det(a1, c1, a2, c2)

    print("\n--- Determinant Values ---")
    print("D  =", D)
    print("Dx =", Dx)
    print("Dy =", Dy)

    if D == 0:
        print("\nCannot solve: D = 0 (Parallel lines or same line).")
        return

    x = Dx / D
    y = Dy / D

    print("\n--- Final Answer ---")
    print(f"x = {x:.4f}")
    print(f"y = {y:.4f}")

# Ask user for the values
print("Enter Equation 1 (a1*x + b1*y = c1):")
a1 = float(input("a1: "))
b1 = float(input("b1: "))
c1 = float(input("c1: "))

print("\nEnter Equation 2 (a2*x + b2*y = c2):")
a2 = float(input("a2: "))
b2 = float(input("b2: "))
c2 = float(input("c2: "))

solve(a1, b1, c1, a2, b2, c2)