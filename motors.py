#MOTOR CLASS
import RPi.GPIO as GPIO
from time import sleep

in1 = 14
in2 = 15
in3 = 2
in4 = 3

en = 22
en2 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

GPIO.setup(en, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)
p1 = GPIO.PWM(en, 1000)
p1.stop()
p2 = GPIO.PWM(en2, 1000)
p2.stop()

print("r-run s-stop f-forward b-backward l-low m-medium h-high dm-frontmiddle dr-frontright dl-frontleft e-exit")

def frontmiddle():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)

def frontright():
    GPIO.output(in1, GPIO.HIGH) # m1 frw
    GPIO.output(in2, GPIO.LOW) # m1 bck
    GPIO.output(in3, GPIO.LOW)# m2 frw
    GPIO.output(in4, GPIO.HIGH) # m2 bck

def frontleft():
    GPIO.output(in1, GPIO.LOW) # m1 frw
    GPIO.output(in2, GPIO.HIGH) # m1 bck
    GPIO.output(in3, GPIO.HIGH)# m2 frw
    GPIO.output(in4, GPIO.LOW) # m2 bck

def forward():
    GPIO.output(in1, GPIO.HIGH)# m1
    GPIO.output(in2, GPIO.LOW) # m1
    GPIO.output(in3, GPIO.HIGH)# m2
    GPIO.output(in4, GPIO.LOW) # m2

def go(speed=100,time=0):
    p1.start(speed) #m1
    p2.start(speed) #m2
    sleep(time)  

def backward(speed=50,time=0):
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH) 
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH) 
    p1.start(speed) 
    p2.start(speed) 

def stop(time=0):
    frontmiddle()
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    sleep(time)

def fright(speed=50,time=0):
    
    frontright()
    go(speed)
    sleep(time)

def fleft(speed=50,time=0):
    
    frontleft()
    go(speed)
    sleep(time)

def bright(speed=50,time=0):
    backward(speed)
    frontright()
    sleep(time)

def bleft(speed=50,time=0):
    backward(speed)
    frontleft()
    sleep(time)
