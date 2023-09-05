import keyboard as kb
from time import sleep
onoff=None

while True:
    if onoff and kb.is_pressed("p"):
        a = kb.is_pressed('q')

        if a is True:
            kb.send('q')
            sleep(0.02)
        elif onoff:
            if kb.is_pressed("ctrl+space"):
                onoff=True
                sleep(0.05)
            else:
                onoff=False
                sleep(0.05)