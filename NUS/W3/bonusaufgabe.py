from math import pi

# Konstanten
e_0 = 8.854e-12;

# Variabeln

r = 6.9e-2
d = 7.6e-3
U = 18.6
alpha = 2.2

# Teilaufgabe 1

print('Teilaufgabe 1: (epsilon_0*epsilon_r* A) / d')

# Teilaufgabe 2

A = (r**2 * pi) / 2

C_0 = (e_0 * 1 * A) / d

print(f'Teilaufgabe 2: {C_0}')

# Teilaufgabe 3

print('Teilaufgabe 3: (epsilon_0 * epsilon_r * U) / d')

# Teilaufgabe 4

Sigma_0 = (C_0 * U) / A

print(f'Teilaufgabe 4: {Sigma_0}')

# Teilaufgabe 5

A_Rotated = A - ((A / pi) * alpha)

C_1 = (e_0 * 1 * A_Rotated) / d

print(f'Teilaufgabe 5: {C_1}')

# Teilaufgabe 5

U_2 = (C_0 * U) / C_1

print(f'Teilaufgabe 6: {U_2}')
