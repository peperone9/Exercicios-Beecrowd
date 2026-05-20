#entradas
consumo = 12
tempo = int(input())
velocidade = int(input())

#processamento
distancia = tempo * velocidade
consumo = distancia / consumo

print(f"{consumo:.3f}")
