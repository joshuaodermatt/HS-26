

#Variabeln
U_Q = 42.9

R_1 = 72.5
R_2 = 40.5
R_3 = 16.3
R_4 = 61.4

# Teilaufgabe 1

R_24 = R_4 + R_2

U_2 = U_Q  * (R_4 / R_24)

print(f'Teilaufgabe 1: {U_2}')

# Teilaufgabe 2

R_ges = 1/((1/R_24) + (1/R_1) + (1/R_3))

print(f'Teilaufgabe 2: {R_ges}')

#Teilaufgabe 3

R_p = (R_2 * R_4) / (R_2 + R_4)

print(f'Teilaufgabe 3: {R_p}')
