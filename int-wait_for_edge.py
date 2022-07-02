#!/usr/bin/env python3

import RPi.GPIO as GPIO

# GPIO BOTAO
BUTTON_GPIO = 16

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    # Total de ciclos, total de vezes do botao pressionado / solto
    contCiclos = 0
    # Contator de botao pressionado
    contPressionado = 0

    while True:
        contCiclos = contCiclos + 1
        # arg1 = channel: numero GPIO - modo BCM (broadcom)
        # arg2 = tipo de interrupcao - FALLING, RISING or BOTH
        # arg3 = timeout - opcional
        GPIO.wait_for_edge(BUTTON_GPIO, GPIO.RISING)
        contPressionado = contPressionado + 1
        print("Botão pressionado! (" + str(contPressionado) + ")")
        print("Ciclos: " + str(contCiclos))
        
        # Limitador de loops
        if contPressionado == 10:
         break;
