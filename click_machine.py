import time
import logging


logger = logging.getLogger('Click Machine')
logger.handlers = []
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)



from Quartz import * # for Mac
from pymouse import PyMouse # PyUserInput required


import math

class Mouse(PyMouse):
    MIN_DISTANCE = 30
    prev_position = None

    def move(self, x, y):
        super(Mouse, self).move(x, y)
        self.prev_position = x, y
    
    def click(self, x, y, button = 1):
        super(Mouse, self).click(x, y, button)
        self.prev_position = x, y
    
    def is_disturbed(self):
        x, y = self.position()
        if self.prev_position:
            px, py = self.prev_position
        else:
            px, py = x, y
        self.prev_position = x, y
        distance = math.sqrt((x - px)**2 + (y - py)**2)
        if distance > self.MIN_DISTANCE:
            return True
        return False
mouse = Mouse()


from collections import namedtuple
    
from abc import ABCMeta, abstractmethod

class MouseDisturbed(Exception): pass
import sys

class Action:
    __metaclass__ = ABCMeta
    @abstractmethod
    def act(self):
        logger.info(`self`)
        if mouse.is_disturbed():
            raw_input('press <ENTER> to continue.')
            for n in reversed(range(2, 12)):
                print '\r' + '<--'.join(map(str, range(1, n))) + ' ',
                sys.stdout.flush()
                time.sleep(1)
                print '\r\033[K',
                sys.stdout.flush()
            # raise MouseDisturbed

class Actions(namedtuple('Actions', ['actions', 'interval']), Action):
    def __new__(cls, actions , interval = 0.03):
        return super(Actions, cls).__new__(cls, actions, interval)
    def act(self):
        super(Actions, self).act()
        for action in self.actions:
            time.sleep(self.interval)
            action.act()

import time
import itertools
class Repeat ( namedtuple('Repeat', ['action', 'times', 'interval' ]), Action ):
    def __new__(cls, action , times = None, interval = 0.03):
        return super(Repeat, cls).__new__(cls, action, times, interval)
    def act(self):
        super(Repeat, self).act()
        if self.times:
            for _ in itertools.repeat(None, self.times):
                time.sleep(self.interval)
                self.action.act()
        else:
            while True:
                time.sleep(self.interval)
                self.action.act()
                
               
class Move(namedtuple('Move', [ 'x', 'y' ]),Action):
    def act(self):
        super(Move, self).act()
        mouse.move(self.x, self.y)

class Click(namedtuple('Click', ['x', 'y']), Action):
    def __new__(cls, x, y ):
        return super(Click, cls).__new__(cls, x,y)
    def act(self):
        super(Click, self).act()
        mouse.click(self.x, self.y)

class Clicks(namedtuple('Clicks', [ 'x', 'y' , 'times', 'interval' ]), Action):
    def __new__(cls, x, y ,  times = 1, interval = 0.03):
        self = super(Clicks, cls).__new__(cls, x, y, times=times, interval=interval)
        self.act = Repeat(Click(x, y), times, interval).act
        return self

class Sleep(namedtuple('Sleep', ['seconds']), Action):
    def __new__(cls, seconds = 1):
        return super(Sleep, cls).__new__(cls, seconds)
    def act(self):
        super(Sleep, self).act()
        time.sleep(self.seconds)



if __name__ == '__main__':
    # Move 
    Move(500, 500).act()
    # Click one time
    Click(200, 200).act()
    # Click 3 times
    Clicks(300, 300, times = 3, interval = 0.5).act()

    # Series actions
    Repeat(
        Actions([
            Move(500, 500),
            Click(200, 200),
            Clicks(300, 300, times = 3, interval = 0.5),
        ], interval = 1)).act()
