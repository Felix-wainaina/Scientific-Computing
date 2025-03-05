import sympy as sp

# Define the symbols
P, e, N = sp.symbols('P e N')
C = P**e % N

# Define the encryption function
encryption_function = sp.Lambda((P, e, N), C)

# Given values
P_value = 7
e_value = 3
N_value = 33

# Compute the ciphertext C
C_value = encryption_function(P_value, e_value, N_value)
print(f"Ciphertext C: {C_value}")

# Compute the modular inverse of P with respect to N for decryption
mod_inverse_P = sp.mod_inverse(P_value, N_value)
print(f"Modular inverse of P with respect to N: {mod_inverse_P}")