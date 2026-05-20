n = int(input())

segundos = n % 60
n = n // 60

minutos = n % 60
n = n // 60

horas = n % 60
n = n // 60

print(f"{horas}:{minutos}:{segundos}")
