n1 = int(input("digite o primeiro número que deseja: "))
n2 = int(input("digite o segundo número que deseja: "))


def transformar_bin(x):
    global resto
    lista = []

    while x >= 2:
        resto = x % 2
        x = x // 2
        lista.append(resto)

    if resto <= 1:
        lista.append(1)

    while len(lista) < 32:
        if (len(lista) % 8) == 0:
            lista.append(" ")
        lista.append(0)

    lista.reverse()

    return lista


num1 = transformar_bin(n1)
num2 = transformar_bin(n2)

print(num1)
print(num2)

