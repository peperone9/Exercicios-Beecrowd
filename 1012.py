linha = input().split(" ")
a = float(linha[0])
b = float(linha[1])
c = float(linha[2])

area = a*c/2
print(f"TRIANGULO: {area:.3f}")
area = c *c * 3.14159 
print(f"CIRCULO: {area:.3f}")
area = (a+b) * c / 2
print(f"TRAPEZIO: {area:.3f}")
area =  b*b
print(f"QUADRADO: {area:.3f}")
area = a * b
print(f"RETANGULO: {area:.3f}")
