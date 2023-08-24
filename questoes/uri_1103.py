while True:
    horas = input().split()

    H1, M1, H2, M2 = horas

    H1 = int(H1)
    M1 = int(M1)
    H2 = int(H2)
    M2 = int(M2)

    if H1 + H2 + M1 + M2 == 0:
        break

    if H1 == 0:
        H1 = 24

    if H2 == 0:
        H2 = 24

    T1 = (H1 * 60) + M1
    T2 = (H2 * 60) + M2

    if T2 > T1:
        dormir = T2 - T1
    else:
        dormir = (24 * 60) - (T1 - T2)

    print(dormir)
