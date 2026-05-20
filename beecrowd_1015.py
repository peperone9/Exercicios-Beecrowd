from math import sqrt
from math import pow
distancia: float

entrada = input().split(" ")
x1 = float(entrada[0])
y1 = float(entrada[1])

entrada = input().split(" ")
x2 = float(entrada[0])
y2 = float(entrada[1])

distancia = sqrt(pow(x2-x1,2) + pow(y2-y1,2))

print(f"{distancia:.4f}")
