import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PWMA = 18
PWMB = 13
AIN1 = 4
AIN2 = 17
BIN1 = 22
BIN2 = 27
ECHO = 2
TRIG = 3

GPIO.setup(PWMA, GPIO.OUT, initial=0)
GPIO.setup(PWMB, GPIO.OUT, initial=0)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(TRIG,GPIO.OUT)


def distance():
    echoTime=0
    pingTime=0
    while True:
        time.sleep(1)
        GPIO.output(TRIG,GPIO.HIGH)
        time.sleep (0.00001)
        GPIO.output(TRIG,GPIO.LOW)
        while GPIO.input(ECHO) == 0:
            pingTime = time.time()
        while GPIO.input(ECHO) == 1:
            echoTime = time.time()
        elapsedTime = echoTime- pingTime
        distance = elapsedTime * 17150  # 343m/s Speed of Sound
        distance = round(distance,0)
        print (int(distance), 'cm   ')
        if distance() < 10:
            forward()
        elif distance() > 10:
            backward()


def forward():
    while True:
        rightmotor = GPIO.PWM(PWMA, 50)  # channel=12 frequency=50Hz
        leftmotor = GPIO.PWM(PWMB, 50)
        rightmotor.start(0)
        leftmotor.start(0)
        rightmotor.ChangeDutyCycle(20)
        leftmotor.ChangeDutyCycle(20)
        time.sleep(1)

        GPIO.output(AIN1, GPIO.HIGH)
        GPIO.output(AIN2, GPIO.LOW)
        GPIO.output(BIN1, GPIO.HIGH)
        GPIO.output(BIN2, GPIO.LOW)
        time.sleep(1)

def backward():
    while True:
        rightmotor = GPIO.PWM(PWMA, 50)  # channel=12 frequency=50Hz
        leftmotor = GPIO.PWM(PWMB, 50)
        rightmotor.start(0)
        leftmotor.start(0)
        rightmotor.ChangeDutyCycle(20)
        leftmotor.ChangeDutyCycle(20)
        time.sleep(1)

        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.HIGH)
        time.sleep(1)

def stop():
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.LOW)
    time.sleep(1)
    GPIO.cleanup()

distance()

#this program perform forward, backward and then stops corespondingly to what the sensor shows.
# The functions needs to be fixt so the can be called from php not from here


