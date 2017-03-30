#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO,setup(17, GPIO.out)

def Blink():
	for i in range(0,3):
		GPIO.output(17,True)
		time.sleep(0.2)
		GPIO.output(17,False)
		time.sleep(0.2)
	time.sleep(5)
	GPIO.setwarnings(False)
	for j in range(0,4):
		print "blink #" + str(J+i)
		GPIO.output(17,True)
		time.sleep(0.2)
		GPIO.output(17,False)
		time.sleep(0.2)
	print "done"
Blink()
time.sleep(5)
Blink()

