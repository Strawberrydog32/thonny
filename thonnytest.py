  
#Add Phidgets Library 
from Phidget22.Phidget import *
from Phidget22.Devices.DigitalOutput import *
from Phidget22.Devices.DigitalInput import *
#Required for sleep statement
import time
import random
import math

"""
class player:
    def __init__(self):
        self.LED = DigitalOutput()
"""

#Create 
redLED = DigitalOutput()
greenLED = DigitalOutput()
redBUTTON = DigitalInput()
greenBUTTON = DigitalInput()

#Address '
greenLED.setHubPort(0)
redLED.setHubPort(1)
redBUTTON.setHubPort(2)
greenBUTTON.setHubPort(3)

greenLED.setIsHubPortDevice(True)
redLED.setIsHubPortDevice(True)
redBUTTON.setIsHubPortDevice(True)
greenBUTTON.setIsHubPortDevice(True)

#Open 
redLED.openWaitForAttachment(1000)
greenLED.openWaitForAttachment(1000)
redBUTTON.openWaitForAttachment(1000)
greenBUTTON.openWaitForAttachment(1000)
#Use your Phidgets
playing = False
scoreG = 0
scoreR = 0
g = None
r = None
winScore = 1000
while(True):
    redLED.setState(redBUTTON.getState())
    greenLED.setState(greenBUTTON.getState())
    if playing:
        if scoreG > winScore or scoreR > winScore:
            redLED.setState(False)
            greenLED.setState(False)
            playing = False
            if scoreG > scoreR:
                for i in range(5):
                    greenLED.setState(True)
                    time.sleep(0.5)
                    greenLED.setState(False)
                    time.sleep(0.5)
            elif scoreR > scoreG:
                for i in range(5):
                    redLED.setState(True)
                    time.sleep(0.5)
                    redLED.setState(False)
                    time.sleep(0.5)
            else:
                for i in range(5):
                    redLED.setState(True)
                    greenLED.setState(True)
                    time.sleep(0.5)
                    redLED.setState(False)
                    greenLED.setState(False)
                    time.sleep(0.5)
            scoreG = 0
            scoreR = 0
        else:
            if g and not greenBUTTON.getState():
                scoreG += 1
                print("Red Score: " + str(scoreR) + " Green Score: " + str(scoreG))
                g = False
            elif not g and greenBUTTON.getState():
                g = True
                
            if r and not redBUTTON.getState():
                scoreR += 1
                print("Red Score: " + str(scoreR) + " Green Score: " + str(scoreG))
                r = False
            elif not g and redBUTTON.getState():
                r = True
        
    else:
        if greenBUTTON.getState() and redBUTTON.getState():
            for i in range(3):
                redLED.setState(True)
                greenLED.setState(True)
                time.sleep(1)
                redLED.setState(False)
                greenLED.setState(False)
                time.sleep(1)
            playing = True
