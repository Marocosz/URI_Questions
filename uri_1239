while True:
    try:
        cod = input()

        cont = len(cod)
        i = 0
        b = 0
        resultado = ""

        for x in range(cont):

            if cod[x] == "_":
                if i == 0:
                    resultado += "<i>"
                    i = 1
                else:
                    resultado += "</i>"
                    i = 0

            elif cod[x] == "*":
                if b == 0:
                    resultado += "<b>"
                    b = 1
                else:
                    resultado += "</b>"
                    b = 0

            else:
                resultado += cod[x]

        print(resultado)

    except(EOFError):
        break
        
