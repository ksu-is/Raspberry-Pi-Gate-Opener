import schedule
import time
import RPi.GPIO as GPIO
from datetime import datetime
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
bc = 0
#bcflip = 0
def task():
    print("Do task now")

def opengate():
    GPIO.output(26, True)
    print("opening gate")

def closegate():
    GPIO.output(26, False)
    print("closing gate")

def crestroninput():
    global bc
    #global bcflip
    input_state = GPIO.input(4)
    if input_state == False:
        #bcflip = 1
        print('Button Pressed')
        opengate()
        bc += 1
    else:
        querrystate()
def querrystate():
    global bc
    time = int(str(datetime.now().time().hour)+str(datetime.now().time().minute))
    if time>2200:
        closegate()
    if bc>=2:
        closegate()
        print("bc")
        bc = 0


schedule.every().day.at("07:00").do(opengate)
schedule.every().day.at("22:00").do(closegate)
try:
    while True:
        schedule.run_pending()
        crestroninput()
        time.sleep(0.2)
finally:
    GPIO.cleanup()