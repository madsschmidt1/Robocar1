import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

IRsensor1 = 7
IRsensor2 = 6
IRsensor3 = 8
PWMA = 18
PWMB = 13
AIN1 = 4
AIN2 = 17
BIN1 = 22
BIN2 = 27

# Pin Setup:
GPIO.setmode(GPIO.BCM)  # Broadcom pin-numbering scheme
GPIO.setup(IRsensor1, GPIO.IN)  # sensor set as input
GPIO.setup(IRsensor2, GPIO.IN)
GPIO.setup(IRsensor3, GPIO.IN)
GPIO.setup(PWMA, GPIO.OUT, initial=0)
GPIO.setup(PWMB, GPIO.OUT, initial=0)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

def main():
    while True:
        forward()

def forward():
    A = GPIO.input(IRsensor1)
    B = GPIO.input(IRsensor2)
    C = GPIO.input(IRsensor3)
    if (A, B, C) == (0, 1, 0):
        rightmotor = GPIO.PWM(PWMA, 30)  # channel=12 frequency=50Hz
        leftmotor = GPIO.PWM(PWMB, 30)
        rightmotor.start(100)
        leftmotor.start(100)
        rightmotor.ChangeDutyCycle(20)
        leftmotor.ChangeDutyCycle(20)
        time.sleep(0.1)

        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.HIGH)
        time.sleep(0.1)

    if (A, B, C) == (1, 1, 0):
        rightmotor = GPIO.PWM(PWMA, 20)  # channel=12 frequency=50Hz
        leftmotor = GPIO.PWM(PWMB, 25)
        rightmotor.start(100)
        leftmotor.start(100)
        rightmotor.ChangeDutyCycle(20)
        leftmotor.ChangeDutyCycle(20)
        time.sleep(0.1)

        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.HIGH)
        time.sleep(0.1)

    if (A, B, C) == (1, 0, 0):
        rightmotor = GPIO.PWM(PWMA, 20)  # channel=12 frequency=50Hz
        leftmotor = GPIO.PWM(PWMB, 30)
        rightmotor.start(100)
        leftmotor.start(100)
        rightmotor.ChangeDutyCycle(20)
        leftmotor.ChangeDutyCycle(20)
        time.sleep(0.1)

        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.HIGH)
        time.sleep(0.1)

    if (A, B, C) == (0, 1, 1):
        rightmotor = GPIO.PWM(PWMA, 20)  # channel=12 frequency=50Hz
        leftmotor = GPIO.PWM(PWMB, 25)
        rightmotor.start(100)
        leftmotor.start(100)
        rightmotor.ChangeDutyCycle(20)
        leftmotor.ChangeDutyCycle(20)
        time.sleep(0.1)

        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.HIGH)
        time.sleep(0.1)

    if (A, B, C) == (0, 0, 1):
        rightmotor = GPIO.PWM(PWMA, 20)  # channel=12 frequency=50Hz
        leftmotor = GPIO.PWM(PWMB, 30)
        rightmotor.start(100)
        leftmotor.start(100)
        rightmotor.ChangeDutyCycle(20)
        leftmotor.ChangeDutyCycle(20)
        time.sleep(0.1)

        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.HIGH)
        time.sleep(0.1)

    if (A, B, C) == (0, 0, 0):
        rightmotor = GPIO.PWM(PWMA, 5)  # channel=12 frequency=50Hz
        leftmotor = GPIO.PWM(PWMB, 5)
        rightmotor.start(100)
        leftmotor.start(100)
        rightmotor.ChangeDutyCycle(20)
        leftmotor.ChangeDutyCycle(20)
        time.sleep(0.1)

        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.LOW)
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.LOW)
        time.sleep(0.1)

    if (A, B, C) == (1, 1, 1):
        print('Error 000 - detecting only white surface')
        rightmotor = GPIO.PWM(PWMA, 30)  # channel=12 frequency=50Hz
        leftmotor = GPIO.PWM(PWMB, 30)
        rightmotor.start(100)
        leftmotor.start(100)
        rightmotor.ChangeDutyCycle(20)
        leftmotor.ChangeDutyCycle(20)
        time.sleep(0.1)

        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.HIGH)
        time.sleep(0.1)

    if (A, B, C) == (1, 0, 1):
        print('Error 101 - it`s going crazy')
        rightmotor = GPIO.PWM(PWMA, 5)  # channel=12 frequency=50Hz
        leftmotor = GPIO.PWM(PWMB, 5)
        rightmotor.start(100)
        leftmotor.start(100)
        rightmotor.ChangeDutyCycle(20)
        leftmotor.ChangeDutyCycle(20)
        time.sleep(0.1)

        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.HIGH)
        time.sleep(0.1)

main()


