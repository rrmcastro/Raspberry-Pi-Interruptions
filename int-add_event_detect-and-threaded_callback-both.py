#!/usr/bin/env python3          
                                
import signal                   
import sys
import RPi.GPIO as GPIO

BUTTON_GPIO = 16
contPressionado = 0
contSolto = 0

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def button_callback(channel):
    global contPressionado
    global contSolto
    if not GPIO.input(BUTTON_GPIO):
        contPressionado = contPressionado + 1
        print("Botão pressionado! (" + str(contPressionado) + ")")
    else:
        contSolto = contSolto + 1
        print("Botao solto! (" + str(contSolto) + ")")

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    GPIO.add_event_detect(BUTTON_GPIO, GPIO.BOTH, 
            callback=button_callback, bouncetime=50)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
    