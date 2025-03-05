import sympy as sp

# Define the matrix A
A = sp.Matrix([[2, 1], [1, 3]])

# Compute the determinant of A
det_A = A.det()
print(f"Determinant of A: {det_A}")

# Find the eigenvalues of A
eigenvalues = A.eigenvals()
print(f"Eigenvalues of A: {eigenvalues}")

# Get the characteristic polynomial
char_poly = A.charpoly()
print(f"Characteristic polynomial: {char_poly.as_expr()}")

# Verify the eigenvalues satisfy the characteristic equation
x = sp.symbols('x')
for eigenvalue in eigenvalues:
    char_eq_value = char_poly.as_expr().subs(x, eigenvalue)
    print(f"Characteristic equation value at eigenvalue {eigenvalue}: {char_eq_value}")
    assert char_eq_value == 0, f"Eigenvalue {eigenvalue} does not satisfy the characteristic equation"

print("All eigenvalues satisfy the characteristic equation.")