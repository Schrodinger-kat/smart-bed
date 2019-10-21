
import RPi.GPIO as GPIO
from tilter import tiltAlert
from time import sleep

SmPin = 22
SnPin = 23
tiltPin = 21

initVal = 0
flag = 0

freq = 50
angle = 45
dc= float(angle)/10 + 2.5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SmPin,GPIO.OUT)
GPIO.setup(SnPin,GPIO.OUT)
#GPIO.setup(tiltPin,GPIO.IN)

m = GPIO.PWM(SmPin,freq)
n = GPIO.PWM(SmPin,freq)

def mew():
    m.start(0)
    n.start(0)
    print("init mew")

def magikarp():
    while True:
        if(GPIO.input(tiltPin)):
            print("*    Tilt Detected    *")
            break
    print("kill while \n return high")
    return 1

def psyduck():
    global initVal
    global flag
    print("init psyduck")
    #sig = magikarp() 
    sig = tiltAlert()

    if sig == 0 and initVal ==0:
        initVal+=1
    elif sig == 1 and initVal == 0:
        flag+=1
        initVal+=1
    elif sig == 1 and initVal == 1:
        flag+=1    
    
    print("kill psyduck",sig,flag,initVal)

def electivire():
    print("init electivire --flag: ",flag)
    
    if flag % 2 != 0:
        print("init motordrive at ",dc,"capacity")
        sleep(1)
        m.ChangeDutyCycle(dc)
        n.ChangeDutyCycle(dc)
    else:
        print("init motordrive at 0 capacity")
        sleep(1)
        m.ChangeDutyCycle(0)
        n.ChangeDutyCycle(0)

def everstone():
    print("init everstone")
    m.stop
    n.stop
    sleep(2)

def mewtwo():
    GPIO.cleanup()

def loop():
    mew()
    psyduck()
    electivire()
    everstone()

if __name__=='__main__':
    try:
        while True:
            loop()
    except KeyboardInterrupt:
        mewtwo()