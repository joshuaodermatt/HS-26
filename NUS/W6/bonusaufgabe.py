import numpy as np

#Variables

U_Q = 20.2
R_1 = 13.1
R_2 = 21.9
R_3 = 15.9
R_4 = 82.0
R_5 = 11.7


#Teilaufgabe 1

# * Bei diesem Ansatz ist etwas falsch. Teilaufgabe 1 alternativ sollte stimmen
# Warscheindlich ein Fehler in der Matrix

GLS = np.array([
#   I, I1, I2, I3, I4, I5
    [-1, 1, 0, 0, 1, 0],
    [ 0, 1, 0, 1, 0, 1],
    [-1, 0, 1, 0, 0, 1],
    [0, R_1, R_2, R_3, 0, 0],
    [0, 0, R_2, 0, R_4, 0],
    [0, R_1, 0, 0, 0, R_5]
])

B = [0, 0, 0, U_Q, 0, 0]

x = np.linalg.solve(GLS, B)

I_3 = x[4]

print(f'Teilaufgabe 1: {I_3}')


# Teilaufgabe 2

U_0 = ( (R_5 / (R_1 + R_5)) - (R_2 / (R_4 + R_2)) ) * U_Q


R_i = ((R_5 * R_1) / (R_1 + R_5)) + ((R_2 * R_4) / (R_4 + R_2))

print(f'Teilaufgabe 2: U_0: {U_0}, R_i: {R_i}')

I_3 = U_0 / (R_i + R_3)

print(f'Teilaufgabe 1 (alternativ): {I_3}')
