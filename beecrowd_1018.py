notas = [100,50,20,10,5,2,1] #notas pro troco
valor: int = -1
def n_cedulas(valor):
    global notas
    print(valor)
    for cedula in notas:
        cedulas = valor // cedula
        print(f"{cedulas} nota(s) de R$ {cedula},00")
        valor = valor % cedula

while valor < 0 or valor > 1000000:
    valor = int(input())
n_cedulas(valor)

