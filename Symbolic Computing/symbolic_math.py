import sympy as sp

# Define the symbol
x = sp.symbols('x')

# Define the loss function
L = 3*x**2 + 2*x - 5

# Compute the first derivative (gradient)
L_prime = sp.diff(L, x)

# Solve for x when the gradient is zero (optimal solution)
optimal_solution = sp.solve(L_prime, x)

# Compute the second derivative
L_double_prime = sp.diff(L_prime, x)

# Evaluate the second derivative at the optimal solution
second_derivative_at_optimal = L_double_prime.evalf(subs={x: optimal_solution[0]})

# Print the results
print(f"Loss function L(x): {L}")
print(f"First derivative (gradient) L'(x): {L_prime}")
print(f"Optimal solution (where L'(x) = 0): x = {optimal_solution[0]}")
print(f"Second derivative L''(x): {L_double_prime}")
print(f"Second derivative at optimal solution: {second_derivative_at_optimal}")

# Determine if it is a minimum or maximum
if second_derivative_at_optimal > 0:
    print("The loss function has a minimum at the optimal solution.")
elif second_derivative_at_optimal < 0:
    print("The loss function has a maximum at the optimal solution.")
else:
    print("The second derivative is zero at the optimal solution, which is a point of inflection.")