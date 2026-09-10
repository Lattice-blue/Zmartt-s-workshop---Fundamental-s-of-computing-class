def det_2x2(p, q, r, s):
    """Calculates the 2x2 determinant: |p  q| / |r  s| = ps - qr"""
    return (p * s) - (q * r)

def solve_cramer_2x2(a1, b1, c1, a2, b2, c2):
    # 1. Compute Main Determinant
    D = det_2x2(a1, b1, a2, b2)
    
    # 2. Compute Coordinate Determinants (Column Substitutions)
    Dx = det_2x2(c1, b1, c2, b2)
    Dy = det_2x2(a1, c1, a2, c2)
    
    # 3. Guard against division by zero
    if D == 0:
        return None, D, Dx, Dy
        
    x = Dx / D
    y = Dy / D
    return (x, y), D, Dx, Dy

# User inputs
if __name__ == "__main__":
    print("Enter values:")
    print("Equation 1: a1*x + b1*y = c1")
    print("Equation 2: a2*x + b2*y = c2\n")
    
    # Ingest coefficients
    a1 = float(input("Enter a1: "))
    b1 = float(input("Enter b1: "))
    c1 = float(input("Enter c1: "))
    
    a2 = float(input("Enter a2: "))
    b2 = float(input("Enter b2: "))
    c2 = float(input("Enter c2: "))
    
    solution, D, Dx, Dy = solve_cramer_2x2(a1, b1, c1, a2, b2, c2)
    
    print("Determinants:")
    print(f"Main Determinant (D)  = {D:.4f}")
    print(f"X Determinant (Dx)    = {Dx:.4f}")
    print(f"Y Determinant (Dy)    = {Dy:.4f}")
    
    if solution is None:
        print("\nResult: No unique solution exists (Determinant D is zero).")
    else:
        x, y = solution
        print(f"\nResult: x = {x:.4f}, y = {y:.4f}")