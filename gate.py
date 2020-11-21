import schedule
import time
#import RPi.GPIO as GPIO
from datetime import datetime 
from gpiozero import LED
"""
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.output(19, True)
GPIO.output(13, True)
GPIO.output(6, True)
GPIO.output(12, True)
GPIO.output(16, True)
GPIO.output(20, True)
GPIO.output(21, True)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
"""
codes = [1234,5678]

bc = 0
global gateclosed
gateclosed=False
global gateopen
gateopen=False
#bcflip = 0
led = LED(17)

def opengate():
    global gateclosed
    global gateopen
    led.on()
    print("opening gate")
    gateopen = True
    gateclosed = False

def closegate():
    global gateclosed
    global gateopen
    led.off()
    print("closing gate")
    gateopen = False
    gateclosed = True


schedule.every().monday.at("07:30").do(opengate)
schedule.every().monday.at("18:30").do(closegate)
schedule.every().tuesday.at("07:30").do(opengate)
schedule.every().tuesday.at("18:30").do(closegate)
schedule.every().wednesday.at("07:30").do(opengate)
schedule.every().wednesday.at("18:30").do(closegate)
schedule.every().thursday.at("07:30").do(opengate)
schedule.every().thursday.at("18:30").do(closegate)
schedule.every().friday.at("07:30").do(opengate)
schedule.every().friday.at("18:30").do(closegate)

while True:
    if gateopen == False:
        codein = input("get code")
        if codein in passcodes:
            opengate()
            print("Gate open")
            time.sleep(45)
            closegate()
            print("Gate closed")
        else:
            print("wrong code")
