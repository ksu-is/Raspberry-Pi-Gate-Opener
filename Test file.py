global gateclosed
gateclosed=False
global gateopen
gateopen=False

def opengate():
    global gateclosed
    global gateopen
    #GPIO.output(26, False)
    print("opening gate")
    gateopen = True
    gateclosed = False

def closegate():
    global gateclosed
    global gateopen
    #GPIO.output(26, True)
    print("closing gate")
    gateopen = False
    gateclosed = True

codes = ["1234", "5678"]

while gateopen == False:
    codein = input("get code")
    if codein in codes:
        opengate()
        print("Gate open")
        time.sleep(45)
        closegate()
        print("Gate closed")
    else:
        print("wrong code")