while True:
    try:
        frase = input()
        frase = frase.lower()

        maiscula = 0

        resultado = ""

        for letra in frase:
            if letra == " ":
                resultado += " "
                continue
            if maiscula == 0:
                resultado += letra.upper()
                maiscula = 1
            else:
                resultado += letra
                maiscula = 0

        print(resultado)

    except(EOFError):
        break
