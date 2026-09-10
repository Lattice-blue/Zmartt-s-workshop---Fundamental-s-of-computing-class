# Program to solve 2 linear equations using Cramer's Rule
#
# Form:
# a1(x) + b1(y) = c1
# a2(x) + b2(y) = c2
#
# Sample Equation to try:
# Equation 1: 2x + 3y = 13
# Equation 2: 4x - 1y = 5
# (Expected Answer: x = 2, y = 3)

print("Solving System of Linear Equations:")
print("Equation 1: a1*x + b1*y = c1")
print("Equation 2: a2*x + b2*y = c2")
print()

# Get inputs from user
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

print("\n--- Results ---")
print("D  =", round(D, 2))
print("Dx =", round(Dx, 2))
print("Dy =", round(Dy, 2))

# Check if we can divide by D
if D == 0:
    print("\nNo unique solution exists because D is 0.")
else:
    x = Dx / D
    y = Dy / D
    print("\nSolution:")
    print("x =", round(x, 2))
    print("y =", round(y, 2))