teste = int(input())

for i in range(teste):
    palavra: list[str] = input().split()

    palavra01 = palavra[0]
    palavra02 = palavra[1]

    nova = ""

    if len(palavra01) <= len(palavra02):  # Se a quantidade de letras da palavra01 for menor que a da palavra02
        for i in range(len(palavra01)):  # Usará o range da quantidade de letras da menor palavra
            nova += palavra01[i]
            nova += palavra02[i]
        nova += palavra02[len(palavra01):]  # E depois pegará o restante das letras da maior palavra e com slacing
        # [inicio: fim: passo] -> [quantidade de letra da menor: até o final]
    else:
        for i in range(len(palavra02)):
            nova += palavra01[i]
            nova += palavra02[i]
        nova += palavra01[len(palavra02):]

    print(nova)
