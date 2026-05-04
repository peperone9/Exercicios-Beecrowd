from math import fabs
linha = input().split(" ")
a = int(linha[0])
b = int(linha[1])
c = int(linha[2])

maior = int((a + b + fabs(a-b)) / 2)
maior = int( (maior + c + fabs(maior-c)) / 2)
print(f"{maior} eh o maior")  
