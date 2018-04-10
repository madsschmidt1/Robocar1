import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

AIN1 = 4
AIN2 = 17
BIN1 = 22
BIN2 = 27
PWMA = 18
PWMB = 13

GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

while True:
    GPIO.output(AIN2, GPIO.HIGH)
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.HIGH)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.setup(PWMA, GPIO.OUT)
    GPIO.setup(PWMB, GPIO.OUT)

    # channel=12 frequency=50Hz
    rightmotor = GPIO.PWM(PWMA, 50)
    rightmotor.start(0)

    leftmotor = GPIO.PWM(PWMB, 50)
    leftmotor.start(0)

    rightmotor.ChangeDutyCycle(20)
    leftmotor.ChangeDutyCycle(20)
    time.sleep(2)

    rightmotor.ChangeDutyCycle(40)
    leftmotor.ChangeDutyCycle(40)
    time.sleep(2)

    rightmotor.ChangeDutyCycle(60)
    leftmotor.ChangeDutyCycle(60)
    time.sleep(2)

    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)

    rightmotor.ChangeDutyCycle(40)
    leftmotor.ChangeDutyCycle(40)
    time.sleep(2)

    rightmotor.ChangeDutyCycle(80)
    leftmotor.ChangeDutyCycle(80)
    time.sleep(2)

    rightmotor.ChangeDutyCycle(0)
    leftmotor.ChangeDutyCycle(0)
    time.sleep(2)

    GPIO.cleanup()

