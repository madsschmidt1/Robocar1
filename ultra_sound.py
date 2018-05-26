import RPi.GPIO as GPIO
import time

# set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BCM)
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
STBY = 26


GPIO.setup(IRsensor1, GPIO.IN)  # sensor set as input
GPIO.setup(IRsensor2, GPIO.IN)
GPIO.setup(IRsensor3, GPIO.IN)
GPIO.setup(PWMA, GPIO.OUT, initial=0)
GPIO.setup(PWMB, GPIO.OUT, initial=0)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

GPIO.setup(STBY, GPIO.OUT)
GPIO.output(STBY, GPIO.HIGH)

rightmotor = GPIO.PWM(PWMA, 50)
leftmotor = GPIO.PWM(PWMB, 50)

rightmotor.start(0)
leftmotor.start(0)

ECHO = 2
TRIG = 3

# A = GPIO.input(IRsensor1)
# B = GPIO.input(IRsensor2)
# C = GPIO.input(IRsensor3)

def initialization():
    GPIO.setup(ECHO, GPIO.IN)  # ECHO
    GPIO.setup(TRIG, GPIO.OUT)  # TRIG

initialization()
time.sleep(0.3)
print("Ultrasonic Measurement")
#GPIO.output(TRIG,GPIO.LOW)


def measure():
        echoTime = 0
        pingTime = 0

        #time.sleep(0.35)
        GPIO.output(TRIG, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(TRIG, GPIO.LOW)
        echoTime = time.time()
        while GPIO.input(ECHO) == 0:
            pingTime = time.time()
        while GPIO.input(ECHO) == 1:
            echoTime = time.time()
        elapsedTime = echoTime - pingTime
        distance = elapsedTime * 17150  # 343m/s Speed of Sound
        distance = round(distance, 0)
        print(distance, " cm")
        return distance


def stop():
    GPIO.output(AIN1, False)
    GPIO.output(AIN2, False)
    GPIO.output(BIN1, False)
    GPIO.output(BIN2, False)
    time.sleep(0.02)


def forward():
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.HIGH)
    rightmotor.ChangeDutyCycle(50)
    leftmotor.ChangeDutyCycle(50)
    #time it turns
    time.sleep(0.8)
    # rightmotor.ChangeDutyCycle(40)
    # leftmotor.ChangeDutyCycle(40)
    # time.sleep(0.7)
    # rightmotor.ChangeDutyCycle(70)
    # leftmotor.ChangeDutyCycle(70)
    # time.sleep(2)

def back():
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)
    rightmotor.ChangeDutyCycle(40)
    leftmotor.ChangeDutyCycle(40)
    time.sleep(0.4)

def right():
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.HIGH)
    rightmotor.ChangeDutyCycle(40)
    leftmotor.ChangeDutyCycle(40)

    # time it turns
    time.sleep(0.02)
def left():
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)
    rightmotor.ChangeDutyCycle(40)
    leftmotor.ChangeDutyCycle(40)

    # time it turns
    time.sleep(0.02)


try:
    while True:
        distance = measure()

        if GPIO.input(IRsensor1) == 1 and GPIO.input(IRsensor3) == 1: \
               # or GPIO.input(IRsensor3) == 1:
        # if (A, B, C) != (0, 0, 0): # Not White
            print('not white, line touched')
            # while A == 1 and B == 1:
            back()
            time.sleep(0.02)
            right()
            time.sleep(0.02)
            stop()
            time.sleep(0.02)

        else:

            if distance <= 90:  # distance of object
                forward()

            elif distance > 90:
                left()
        time.sleep(0.02)
# except KeyboardInterrupt:
    # cleanup the GPIO pins before ending
finally:
    GPIO.cleanup()

