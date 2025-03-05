import sympy as sp

# Define the Laplace variable s and time variable t
s, t = sp.symbols('s t')

# Define the Laplace Transform of the system equation H(s)
H_s = 1 / (s**2 + 3*s + 2)

# Factor the denominator symbolically
denominator = s**2 + 3*s + 2
factored_denominator = sp.factor(denominator)
print(f"Factored denominator: {factored_denominator}")

# Compute the inverse Laplace Transform to find h(t)
h_t = sp.inverse_laplace_transform(H_s, s, t)
print(f"Inverse Laplace Transform h(t): {h_t}")

# Find the poles of the system
poles = sp.solve(denominator, s)
print(f"Poles of the system: {poles}")