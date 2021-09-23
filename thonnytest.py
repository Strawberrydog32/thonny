"""
Docstring
"""
import sys
import time

# import random
# import math
# from Phidget22.Phidget import  *
from Phidget22.Devices.DigitalOutput import DigitalOutput
from Phidget22.Devices.DigitalInput import DigitalInput


WINSCORE = 10


class Logger:
    """
    A Logger for debugging
    """
    def __init__(self, file=sys.stdout):
        self.out_file = file
        self.log_levels

    def set_level(self, level):
        if level in self.log_levels:
            

    def log(self, message, level="info"):
        print(message, file=self.out_file)


class Player:
    def __init__(self, Led_port, Button_port, name):
        self.name = name

        self.led = DigitalOutput()
        self.led.setHubPort(Led_port)
        self.led.setIsHubPortDevice(True)
        self.led.openWaitForAttachment(1000)

        self.button = DigitalInput()
        self.button.setHubPort(Button_port)
        self.button.setIsHubPortDevice(True)
        self.button.openWaitForAttachment(1000)

        self.score = 0
        self.previous_state = None

    def update(self):
        self.led.setState(self.button.getState())

    def set_previous_state(self, state):
        self.previous_state = state

    def reset(self):
        self.score = 0
        self.previous_state = None

    @classmethod
    def flash(cls, players, count, delay):  # update this to be a class method
        for a in range(count):
            for player in players:
                i.led.setState(True)
            time.sleep(delay)
            for player in players:
                i.led.setState(False)
            time.sleep(delay)

logger = Logger()
red = Player(0, 2, "Red")
green = Player(1, 3, "Green")
PLAYERS = [red, green]
playing = False

while True:
    for i in PLAYERS:
        i.update()
    if playing:
        if any(((i.score >= WINSCORE) for i in PLAYERS)):
            playing = False
            Player.flash([sorted(PLAYERS, key=lambda x: x.score)[0]], 3, 0.5)
            for i in PLAYERS:
                i.reset()

        else:
            for i in PLAYERS:
                if i.previous_state and not i.button.getState():
                    i.score += 1
                    # print("Red Score: " + str(scoreR) + " Green Score: " + str(scoreG))

            for i in PLAYERS:
                i.set_previous_state(i.button.getState())

    else:
        if all(i.button.getState() for i in PLAYERS):
            Player.flash(PLAYERS, 3, 0.5)
            playing = True
