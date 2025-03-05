import sympy as sp

# Define the symbol
x = sp.symbols('x')

# Define the cost function C(x)
C = 5*x**3 - 10*x**2 + 4*x + 3

# Compute the first derivative (gradient)
C_prime = sp.diff(C, x)
print(f"First derivative (gradient) C'(x): {C_prime}")

# Solve for x when the gradient is zero (optimal solution)
optimal_solutions = sp.solve(C_prime, x)
print(f"Optimal solutions (where C'(x) = 0): {optimal_solutions}")

# Compute the second derivative
C_double_prime = sp.diff(C_prime, x)
print(f"Second derivative C''(x): {C_double_prime}")

# Evaluate the second derivative at the optimal solutions
for solution in optimal_solutions:
    second_derivative_value = C_double_prime.evalf(subs={x: solution})
    print(f"Second derivative at x = {solution}: {second_derivative_value}")
    if second_derivative_value > 0:
        print(f"x = {solution} corresponds to a minimum cost.")
    elif second_derivative_value < 0:
        print(f"x = {solution} corresponds to a maximum cost.")
    else:
        print(f"x = {solution} is a point of inflection.")

# Interpretation for decision-making
print("\nInterpretation for decision-making:")
for solution in optimal_solutions:
    if C_double_prime.evalf(subs={x: solution}) > 0:
        print(f"The number of AI startups funded should be {solution} to minimi