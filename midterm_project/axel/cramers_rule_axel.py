# Program to solve two linear equations using Cramer's Rule
# Example problem:
#   Equation 1: 3x + 2y = 16
#   Equation 2: 1x - 4y = -4

print("Cramer's Rule Solver (2x2)")
print("Equation 1: a1*x + b1*y = c1  (Example: 3x + 2y = 16)")
print("Equation 2: a2*x + b2*y = c2  (Example: 1x - 4y = -4)")
print("-" * 35)

# Get numbers from user
a1 = float(input("Enter a1: "))
b1 = float(input("Enter b1: "))
c1 = float(input("Enter c1: "))

a2 = float(input("Enter a2: "))
b2 = float(input("Enter b2: "))
c2 = float(input("Enter c2: "))

# Calculate determinants
D = (a1 * b2) - (b1 * a2)
Dx = (c1 * b2) - (b1 * c2)
Dy = (a1 * c2) - (c1 * a2)

print("\nDeterminants:")
print("D  =", round(D, 2))
print("Dx =", round(Dx, 2))
print("Dy =", round(Dy, 2))

# Find x and y
if D == 0:
    print("\nNo unique solution (cannot divide by zero).")
else:
    x = Dx / D
    y = Dy / D
    print("\nSolution:")
    print("x =", round(x, 2))
    print("y =", round(y, 2))