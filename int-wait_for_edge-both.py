#!/usr/bin/env python3

import RPi.GPIO as GPIO

BUTTON_GPIO = 16

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # Total de ciclos, total de vezes do botao pressionado / solto
    contCiclos = 0
    contPressionado = 0
    contSolto = 0

    while True:
        contCiclos = contCiclos + 1
        # arg1 = channel: here the GPIO number - BCM mode
        # arg2 = type of interrupt - FALLING, RISING or BOTH
        # arg3 = timeout - opcional
        GPIO.wait_for_edge(BUTTON_GPIO, GPIO.BOTH)
        
        # ainda sem mecanismo de debounce
        if not GPIO.input(BUTTON_GPIO):
            contPressionado = contPressionado + 1
            print("Botão pressionado! (" + str(contPressionado) + ")")
        else:
            contSolto = contSolto + 1
            print("Botão solto! (" + str(contSolto) + ")")
            
        print("Ciclos: " + str(contCiclos))
        
        if contPressionado == 10 or contSolto == 10:
            break;

