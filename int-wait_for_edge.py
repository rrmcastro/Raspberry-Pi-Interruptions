#!/usr/bin/env python3

import RPi.GPIO as GPIO

BUTTON_GPIO = 16

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    contCiclos = 0
    contBotao = 0

    while True:
        contCiclos = contCiclos + 1
        # arg1 = channel: here the GPIO number - BCM mode
        # arg2 = type of interrupt - FALLING, RISING or BOTH
        # arg3 = timeout - opcional
        GPIO.wait_for_edge(BUTTON_GPIO, GPIO.RISING)
        contBotao = contBotao + 1
        print("Botão pressionado! (" + str(contBotao) + ")")
        print("Ciclos: " + str(contCiclos))
        
        if contBotao == 10:
         break;
