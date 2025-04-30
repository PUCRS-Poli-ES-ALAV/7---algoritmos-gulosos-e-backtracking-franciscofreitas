def calculaTroco(moedas, valor):
    resultado = []
    moedas.sort(reverse = True)
    for moeda in moedas:
        while valor >= moeda:
            resultado.append(moeda)
            valor -= moeda

    return resultado

troco = 289
moedas = [100, 25, 10, 5, 1]
resultado = calculaTroco(moedas, troco)
print(len(resultado), "moedas utilizadas:", resultado)
