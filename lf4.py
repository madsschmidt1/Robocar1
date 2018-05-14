import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(11, GPIO.OUT)
GPIO.setmode(13, GPIO.OUT)
GPIO.setmode(15, GPIO.OUT)
GPIO.setmode(16, GPIO.OUT)

GPIO.setmode(8, GPIO.IN)
GPIO.setmode(6, GPIO.IN)
GPIO.setmode(7, GPIO.IN)

