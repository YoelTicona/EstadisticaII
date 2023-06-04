# Regresion lineal #
def coeficientes(x, y):
    muX = np.mean(x)
    muY = np.mean(y)
    # Hallamos b1
    up = 0
    for i in range(n):
        up += (x[i] - muX)*(y[i] - muY)
    down = 0
    for i in range(n):
        down += (x[i] - muX)**2
    b1 = round(up/down, 4)

    # Hallamos b0
    b0 = round((muY - (b1*muX)), 4)
    return b0, b1

def sumaCuadrados(x, y, b0, b1):
    muX = np.mean(x)
    muY = np.mean(y)
    # SCE #
    y_estimado = []
    for i in range(n):
        y_estimado.append(b0 + b1*x[i])
    SCE = 0
    for i in range(n):
        SCE += (y[i] - y_estimado[i])**2

    # STC #
    STC = 0
    for i in range(n):
        STC += (y[i] - muY)**2

    # SCR #
    SCR = STC - SCE
    return SCE, STC, SCR
    
# ===== PROGRAMA PRINCIPAL ===== #
import numpy as np
import math
x = [2, 4, 3,  4,  6,  5,  6] # Datos por defecto
y = [8, 9, 9, 12, 16, 15, 21] # Datos por defecto
n = 7

# Hallando los coeficientes
b0, b1 = coeficientes(x, y)
print("* Ecuación de la regresión lineal estimada:")
print("y =", b0, "+", b1,"x")

print("\n* Tipos de suma de cuadrados")
SCE, STC, SCR = sumaCuadrados(x, y, b0, b1)
print("SCE:", SCE)
print("STC:", STC)
print("SCR:", SCR)

#r^2#
print("\n* COEFICIENTE DE DETERMINACION")
r_2 = round(SCR/STC, 4)
print("r^2:", r_2)
print("COEFICIENTE DE CORRELACION:")
r = round(math.sqrt(r_2), 4)
if(b1 >= 0):
    print("r = +", round(r, 4))
else:
    print("r = -", round(r, 4))
