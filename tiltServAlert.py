
import RPi.GPIO as GPIO
from time import sleep

SmPin = 22
SnPin = 23
tiltPin = 21

counter = 0
flag = 0

freq = 50
angle1 = 45
angle2 = 145
dc1 = float(angle1)/10 + 2.5
dc2 = float(angle2)/10 + 2.5


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SmPin,GPIO.OUT)
GPIO.setup(SnPin,GPIO.OUT)
GPIO.setup(tiltPin,GPIO.IN, pull_up_down=GPIO.PUD_UP)

def mew():
    m = GPIO.PWM(SmPin,freq)
    n = GPIO.PWM(SmPin,freq)
    m.start(2.5)
    n.start(2.5)
    print("init mew suceeded")

def alert(ev=None):
    print("Tilt Detected :)")
    mew()
    sig = True
    global counter
    counter = counter + 1
    electivire()

def electivire():
    print("init electivire",counter)
    m = GPIO.PWM(SmPin,freq)
    n = GPIO.PWM(SmPin,freq)

    if counter%2 != 0:
        print("init motordrive at ",dc1,"capacity")
        sleep(1)
        m.ChangeDutyCycle(dc1)
        n.ChangeDutyCycle(dc1)
    else:
        print("init motordrive at ",dc2," capacity")
        sleep(1)
        m.ChangeDutyCycle(dc2)
        n.ChangeDutyCycle(dc2)

def everstone():
    print("init everstone")
    m = GPIO.PWM(SmPin,freq)
    n = GPIO.PWM(SmPin,freq)
    m.stop
    n.stop
    sleep(2)

def mewtwo():
    GPIO.cleanup()

def loop():
    mew()
    GPIO.add_event_detect(tiltPin, GPIO.FALLING, callback=alert, bouncetime=100)
    everstone()

if __name__=='__main__':
    try:
        loop()
    except KeyboardInterrupt:
        mewtwo()