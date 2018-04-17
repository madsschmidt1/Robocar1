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

GPIO.setup(PWMA, GPIO.OUT, initial=0)
GPIO.setup(PWMB, GPIO.OUT, initial=0)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)


while True:
    rightmotor = GPIO.PWM(PWMA, 50)  # channel=12 frequency=50Hz
    leftmotor = GPIO.PWM(PWMB, 50)
    rightmotor.start(0)
    leftmotor.start(0)


    rightmotor.ChangeDutyCycle(0)
    leftmotor.ChangeDutyCycle(0)
    time.sleep(2)
    rightmotor.ChangeDutyCycle(0)
    leftmotor.ChangeDutyCycle(0)


GPIO.output(AIN1, GPIO.HIGH)
GPIO.output(AIN2, GPIO.LOW)
GPIO.output(BIN1, GPIO.LOW)
GPIO.output(BIN2, GPIO.HIGH)
time.sleep(1)