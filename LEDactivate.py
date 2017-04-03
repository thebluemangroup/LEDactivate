import RPi.GPIO as GPIO
from time import sleep
class LEDactivate:

    def __init__(self):
        self.Pin_OUT1 = 27  # Red
        self.Pin_OUT2 = 26  # Blue
        self.Pin_OUT3 = 25  # Green
        self.Freq = 100
        GPIO.setmode(GPIO.BCM)  # set pin mode to broadcom
        GPIO.setup(self.Pin_OUT1, GPIO.OUT)  # gpio pin 17 (physical pin 11) set to output
        GPIO.setup(self.Pin_OUT2, GPIO.OUT)  # gpio pin 17 (physical pin 11) set to output
        GPIO.setup(self.Pin_OUT3, GPIO.OUT)  # gpio pin 17 (physical pin 11) set to output
        GPIO.output(self.Pin_OUT1, False)  # LED off
        GPIO.output(self.Pin_OUT2, False)  # LED off
        GPIO.output(self.Pin_OUT3, False)  # LED off
        self.RED = GPIO.PWM(self.Pin_OUT1, self.Freq)
        self.RED.start(0)
        self.GREEN = GPIO.PWM(self.Pin_OUT2, self.Freq)
        self.GREEN.start(0)
        self.BLUE = GPIO.PWM(self.Pin_OUT3, self.Freq)
        self.BLUE.start(0)
    def Blink(self, ColorNumber, BlinkNumber, DurOn, DurOff, intensityR, intensityG, intensityB):
        self.color = int(ColorNumber)
        self.DurOn = DurOn
        self.DurOff = DurOff
        self.blink = int(BlinkNumber)
        self.intensityR = intensityR
        self.intensityG = intensityG
        self.intensityB = intensityB
        if self.color == 1:
            for i in range(0, self.blink):
                self.RED.ChangeDutyCycle(self.intensityR)  # LED on
                sleep(self.DurOn)
                self.RED.ChangeDutyCycle(0)  # LED off
                sleep(self.DurOff)

        if self.color == 2:
            for i in range(0, self.blink):
                self.GREEN.ChangeDutyCycle(self.intensityG)  # LED on
                sleep(self.DurOn)  # wait 1 second
                self.GREEN.ChangeDutyCycle(0)  # LED off
                sleep(self.DurOff)  # wait 1 second

        if self.color == 4:
            for i in range(0, self.blink):
                self.BLUE.ChangeDutyCycle(self.intensityB)  # LED on
                sleep(self.DurOn) # wait 1 second
                self.BLUE.ChangeDutyCycle(0)  # LED off
                sleep(self.DurOff)  # wait 1 second

        if self.color == 3:
            for i in range(0, self.blink):
                self.RED.ChangeDutyCycle(self.intensityR)  # LED on
                self.GREEN.ChangeDutyCycle(self.intensityG)  # LED on
                sleep(self.DurOn)  # wait 1 second
                self.RED.ChangeDutyCycle(0)  # LED off
                self.GREEN.ChangeDutyCycle(0)  # LED off
                sleep(self.DurOff)  # wait 1 second

        if self.color == 5:
            for i in range(0, self.blink):
                self.RED.ChangeDutyCycle(self.intensityR)  # LED on
                self.BLUE.ChangeDutyCycle(self.intensityB)  # LED on
                sleep(self.DurOn)  # wait 1 second
                self.RED.ChangeDutyCycle(0)  # LED off
                self.BLUE.ChangeDutyCycle(0)  # LED off
                sleep(self.DurOff)  # wait 1 second

        if self.color == 6:
            for i in range(0, self.blink):
                self.GREEN.ChangeDutyCycle(self.intensityG)  # LED on
                self.BLUE.ChangeDutyCycle(self.intensityB)  # LED on
                sleep(self.DurOn)  # wait 1 second
                self.GREEN.ChangeDutyCycle(0)  # LED off
                self.BLUE.ChangeDutyCycle(0)  # LED off
                sleep(self.DurOff)  # wait 1 second

        if self.color == 7:
            for i in range(0, self.blink):
                self.RED.ChangeDutyCycle(self.intensityR)  # LED on
                self.GREEN.ChangeDutyCycle(self.intensityG)  # LED on
                self.BLUE.ChangeDutyCycle(self.intensityB)  # LED on
                sleep(self.DurOn)  # wait 1 second
                self.RED.ChangeDutyCycle(0)  # LED off
                self.GREEN.ChangeDutyCycle(0)  # LED off
                self.BLUE.ChangeDutyCycle(0)  # LED off
                sleep(self.DurOff)
        self.RED.ChangeDutyCycle(0)  # LED off
        self.GREEN.ChangeDutyCycle(0)  # LED off
        self.BLUE.ChangeDutyCycle(0)  # LED off

    def Solid(self, ColorNumber, DurOn, intensityR, intensityG, intensityB):
        self.color = int(ColorNumber)
        self.DurOn = DurOn
        self.intensityR = intensityR
        self.intensityG = intensityG
        self.intensityB = intensityB
        if self.color == 1:
                self.RED.ChangeDutyCycle(self.intensityR)  # LED on
                sleep(self.DurOn)

        if self.color == 2:
                self.GREEN.ChangeDutyCycle(self.intensityG)  # LED on
                sleep(self.DurOn)  # wait 1 second

        if self.color == 4:
                self.BLUE.ChangeDutyCycle(self.intensityB)  # LED on
                sleep(self.DurOn)  # wait 1 second

        if self.color == 3:
                self.RED.ChangeDutyCycle(self.intensityR)  # LED on
                self.GREEN.ChangeDutyCycle(self.intensityG)  # LED on
                sleep(self.DurOn)  # wait 1 second

        if self.color == 5:
                self.RED.ChangeDutyCycle(self.intensityR)  # LED on
                self.BLUE.ChangeDutyCycle(self.intensityB)  # LED on
                sleep(self.DurOn)  # wait 1 second

        if self.color == 6:
                self.GREEN.ChangeDutyCycle(self.intensityG)  # LED on
                self.BLUE.ChangeDutyCycle(self.intensityB)  # LED on
                sleep(self.DurOn)  # wait 1 second

        if self.color == 7:
                self.RED.ChangeDutyCycle(self.intensityR)  # LED on
                self.GREEN.ChangeDutyCycle(self.intensityG)  # LED on
                self.BLUE.ChangeDutyCycle(self.intensityB)  # LED on
                sleep(self.DurOn)  # wait 1 second
        self.RED.ChangeDutyCycle(0)  # LED off
        self.GREEN.ChangeDutyCycle(0)  # LED off
        self.BLUE.ChangeDutyCycle(0)  # LED off

LEDtest1 = LEDactivate()
LEDtest2 = LEDactivate()
for level in range(1,8):
    LEDtest2.Solid(level,3,10,100,30)
    LEDtest1.Blink(level,3,1,1,10,100,30)
