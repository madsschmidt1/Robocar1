import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

IRsensor1 = 6
IRsensor2 = 7
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
    if (A, B, C) == (0, 1, 0): # the car goes forward
        rightmotor = GPIO.PWM(PWMA, 30)  # channel=12 frequency=50Hz
        leftmotor = GPIO.PWM(PWMB, 30)
        rightmotor.start(100)
        rightmotor.ChangeDutyCycle(20)
        leftmotor.ChangeDutyCycle(20)
        time.sleep(1)

        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.HIGH)
        time.sleep(1)

    if (A, B, C) == (1, 1, 0): # the car goes slightly LEFT
        rightmotor = GPIO.PWM(PWMA, 25)  # channel=12 frequency=50Hz
        leftmotor = GPIO.PWM(PWMB, 30)
        rightmotor.start(100)
        leftmotor.start(100)
        rightmotor.ChangeDutyCycle(20)
        leftmotor.ChangeDutyCycle(20)
        time.sleep(1)

        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.HIGH)
        time.sleep(1)

    if (A, B, C) == (1, 0, 0): # the car goes LEFT
        rightmotor = GPIO.PWM(PWMA, 25)  # channel=12 frequency=50Hz
        leftmotor = GPIO.PWM(PWMB, 35)
        rightmotor.start(100)
        leftmotor.start(100)
        rightmotor.ChangeDutyCycle(20)
        leftmotor.ChangeDutyCycle(20)
        time.sleep(1)

        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.HIGH)
        time.sleep(1)

   if (A, B, C) == (0, 1, 1): # the car goes slightly RIGHT
        rightmotor = GPIO.PWM(PWMA, 30)  # channel=12 frequency=50Hz
        leftmotor = GPIO.PWM(PWMB, 25)
        rightmotor.start(100)
        leftmotor.start(100)
        rightmotor.ChangeDutyCycle(20)
        leftmotor.ChangeDutyCycle(20)
        time.sleep(1)

        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.HIGH)
        time.sleep(1)

   if (A, B, C) == (0, 0, 1): # the car goes RIGHT
        rightmotor = GPIO.PWM(PWMA, 35)  # channel=12 frequency=50Hz
        leftmotor = GPIO.PWM(PWMB, 25)
        rightmotor.start(100)
        leftmotor.start(100)
        rightmotor.ChangeDutyCycle(20)
        leftmotor.ChangeDutyCycle(20)
        time.sleep(1)

        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.HIGH)
        time.sleep(1)

    if (A, B, C) == (0, 0, 0): # the car STOPS
        rightmotor = GPIO.PWM(PWMA, 10)  # channel=12 frequency=50Hz
        leftmotor = GPIO.PWM(PWMB, 10)
        rightmotor.start(100)
        leftmotor.start(100)
        rightmotor.ChangeDutyCycle(20)
        leftmotor.ChangeDutyCycle(20)
        time.sleep(1)

        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.LOW)
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.LOW)
        time.sleep(1)

main()

