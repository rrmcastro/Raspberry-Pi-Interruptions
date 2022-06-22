#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

# Contantes de Pinagem
BUTTON_GPIO = 16

if __name__ == '__main__':
    # Modo Broadcom
    GPIO.setmode(GPIO.BCM)
    # Config GPIO 16 como botão input
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    pressed = False
    contCiclos = 0
    contBotao = 0    

    while True:
        # botão pressionado quando pino é LOW
        if not GPIO.input(BUTTON_GPIO):
            if not pressed:
                contBotao = contBotao + 1
                print("Botão pressionado! (" + str(contBotao) + ")")
                pressed = True
        # botão não pressionao (ou solto)
        else:
            pressed = False
        
        if contBotao == 10 or contCiclos == 100:
            break;
        
        contCiclos = contCiclos + 1
        print("Ciclos: " + str(contCiclos))
        time.sleep(0.1) # Frequência 10Hz
