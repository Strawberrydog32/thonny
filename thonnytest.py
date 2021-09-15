from Phidget22.Phidget import *
from Phidget22.Devices.DigitalOutput import *
from Phidget22.Devices.DigitalInput import *
import time
import random
import math


WINSCORE = 1000

class player:
    def __init__(self, Led_port, Button):
        
        self.Led = DigitalOutput()
        self.Led.setHubPort(Led_port)
        self.Led.setIsHubPortDevice(True)
        self.Led.openWaitForAttachment(1000)
        
        self.Button = DigitalInput()
        self.Button.setHubPort(Button_port)
        self.Button.setIsHubPortDevice(True)
        self.Button.openWaitForAttachment(1000)
        
        self.score = 0
        self.previous_state = None
        
    def update(self):
        self.Led.setState(self.Button.getState())
        
    @classmethod
    def flash(cls, players, count, delay): #update this to be a class method
        for a in range(count)
            [i.Led.setState(True) for i in players]
            time.sleep(delay)
            [i.Led.setState(False) for i in players]
            time.sleep(delay)



red = player(0, 2)
green = player(1, 3)
players = [red, green]
playing = False

while(True):
    [i.update() for i in players]
    if playing:
        if any([(i.score >= WINSCORE) for i in players]):
            playing = False
            player.flash([sorted(players, key=lambda x: x.score)[0]], 3, 0.5)
            scoreG = 0
            scoreR = 0
        else:
            for i in players:
                if i.previous_state and not i.Button.getState():
                    i.score += 1
                    print("Red Score: " + str(scoreR) + " Green Score: " + str(scoreG))
                
            [i.previous_state = i.Button.getState() for i in players]
        
    else:
        if all(i.Button.getState() for i in players):
            for i in range(3):
                player.flash(players, 3, 0.5)
            playing = True
