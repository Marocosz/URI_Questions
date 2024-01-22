import keyboard as kb
from time import sleep

onoff = None

while True:
    ativar = kb.is_pressed('ctrl+space')

    if ativar is True:
        print('on')
        onoff = 1

    sleep(0.05)

    while onoff:
        desativar = kb.is_pressed('p')

        if desativar is True:
            print('off')
            onoff = 0 

        a = kb.is_pressed('q')

        if a is True:
            kb.send('q')
            sleep(0.02)
