# Variabeln

b = 6.6e-2
h = 11.8e-2
I = 5.0
l_1 = 102.3e-2
k_1 = 115e6
l_2 = 42.6e-2
k_2 = 68e6

# Teilaufgabe 1

A_1 = (h * b)

j_1 = I / A_1

print(f'Teilaufgabe 1: {j_1}');

# Teilaufgabe 2

A_2 = (h * b)

j_2 = I / A_2

print(f'Teilaufgabe 1: {j_2}');

# Teilaufgabe 3

E_1 = j_1 / k_1

print(f'Teilaufgabe 3: {E_1}')

# Teilaufgabe 4

E_2 = j_2 / k_2

print(f'Teilaufgabe 4: {E_2}')

# Teilaufgabe 5


U_1 = E_1 * l_1
U_2 = E_2 * l_2

U_tot = U_1 + U_2;

print(f'Teilaufgabe 5: {U_tot}')

# Teilaufgabe 6

R_1 = U_1 / I
R_2 = U_2 / I

R_ges = R_1 + R_2

print(f'Teilaufgabe 6: {R_ges}')

# Teilaufgabe 7

P_1 = I**2 * R_1

print(f'Teilaufgabe 7: {P_1}')

# Teilaufgabe 8

P_2 = I**2 * R_2

print(f'Teilaufgabe 7: {P_2}')
