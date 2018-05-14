import RPi.GPIO as GPIO
import time

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
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(IRsensor1, GPIO.IN) # sensor set as input
GPIO.setup(IRsensor2, GPIO.IN)
GPIO.setup(IRsensor3, GPIO.IN)
GPIO.setup(PWMA, GPIO.OUT, initial=0)
GPIO.setup(PWMB, GPIO.OUT, initial=0)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)


while True:
    A = GPIO.input(IRsensor1)
    B = GPIO.input(IRsensor2)
    C = GPIO.input(IRsensor3)
    print (A, B, C)
    time.sleep(0.01)

    if (A, B, C) == (1, 1, 1):
        forward()
    elif (A, B, C) == (1, 1, 0):
        left()
    elif (A, B, C) == (1, 0, 0):
        left_faster()
    elif (A, B, C) == (0, 1, 1):
        right()
    elif (A, B, C) == (0, 0, 1):
        right_faster()
    elif (A, B, C) == (0, 0, 0):
        backward()

    def forward():
        while True:
            rightmotor = GPIO.PWM(PWMA, 50)  # channel=12 frequency=50Hz
            leftmotor = GPIO.PWM(PWMB, 50)
            rightmotor.start(100)
            leftmotor.start(100)
            rightmotor.ChangeDutyCycle(20)
            leftmotor.ChangeDutyCycle(20)
            time.sleep(1)

            GPIO.output(AIN1, GPIO.HIGH)
            GPIO.output(AIN2, GPIO.LOW)
            GPIO.output(BIN1, GPIO.HIGH)
            GPIO.output(BIN2, GPIO.LOW)
            time.sleep(1)

    def left():
        while True:
            rightmotor = GPIO.PWM(PWMA, 55)  # channel=12 frequency=50Hz
            leftmotor = GPIO.PWM(PWMB, 45)
            rightmotor.start(100)
            leftmotor.start(100)
            rightmotor.ChangeDutyCycle(20)
            leftmotor.ChangeDutyCycle(20)
            time.sleep(1)

            GPIO.output(AIN1, GPIO.HIGH)
            GPIO.output(AIN2, GPIO.LOW)
            GPIO.output(BIN1, GPIO.HIGH)
            GPIO.output(BIN2, GPIO.LOW)
            time.sleep(1)
            forward()

    def left_faster():
        while True:
            rightmotor = GPIO.PWM(PWMA, 60)  # channel=12 frequency=50Hz
            leftmotor = GPIO.PWM(PWMB, 40)
            rightmotor.start(100)
            leftmotor.start(100)
            rightmotor.ChangeDutyCycle(20)
            leftmotor.ChangeDutyCycle(20)
            time.sleep(1)

            GPIO.output(AIN1, GPIO.HIGH)
            GPIO.output(AIN2, GPIO.LOW)
            GPIO.output(BIN1, GPIO.HIGH)
            GPIO.output(BIN2, GPIO.LOW)
            time.sleep(1)
            forward()


    def right():
        while True:
            rightmotor = GPIO.PWM(PWMA, 45)  # channel=12 frequency=50Hz
            leftmotor = GPIO.PWM(PWMB, 55)
            rightmotor.start(100)
            leftmotor.start(100)
            rightmotor.ChangeDutyCycle(20)
            leftmotor.ChangeDutyCycle(20)
            time.sleep(1)

            GPIO.output(AIN1, GPIO.HIGH)
            GPIO.output(AIN2, GPIO.LOW)
            GPIO.output(BIN1, GPIO.HIGH)
            GPIO.output(BIN2, GPIO.LOW)
            time.sleep(1)
            forward()


    def right_faster():
        while True:
            rightmotor = GPIO.PWM(PWMA, 40)  # channel=12 frequency=50Hz
            leftmotor = GPIO.PWM(PWMB, 60)
            rightmotor.start(100)
            leftmotor.start(100)
            rightmotor.ChangeDutyCycle(20)
            leftmotor.ChangeDutyCycle(20)
            time.sleep(1)

            GPIO.output(AIN1, GPIO.HIGH)
            GPIO.output(AIN2, GPIO.LOW)
            GPIO.output(BIN1, GPIO.HIGH)
            GPIO.output(BIN2, GPIO.LOW)
            time.sleep(1)
            forward()

    def backward():
        while True:
            rightmotor = GPIO.PWM(PWMA, 50)  # channel=12 frequency=50Hz
            leftmotor = GPIO.PWM(PWMB, 50)
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

    def stop():
        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.LOW)
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.LOW)
        time.sleep(1)
        GPIO.cleanup()
