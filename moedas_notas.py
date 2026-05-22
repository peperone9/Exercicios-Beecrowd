def cedulas(valor, notas, moedas):
    print("NOTAS:")
    for nota in notas:
        print(f"{int(valor // nota)} nota(s) de R$ {nota:.2f}")
        valor = valor % nota
    print("MOEDAS:")
    for moeda in moedas:
        print(f"{int(valor // moeda)} moeda(s) de R$ {moeda:.2f}")
        valor = valor % moeda

n: float = -1
while n < 0 or n > 1000000.00:
    n = float(input())
notas = [100,50,20,10,5,2]
moedas = [1.0,0.5,0.25, 0.1, 0.05, 0.01]
cedulas(n, notas, moedas)
