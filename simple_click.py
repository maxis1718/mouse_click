# codingL utf-8

from Quartz import * # for Mac
from pymouse import PyMouse # PyUserInput required
import math, time, logging

class ClickerHeroes(object):
    """
    simple click tool for ClickerHeroes - just perform clicks

    Example
    =======

    >> from simple_click import ClickerHeroes
    >> ch = ClickerHeroes(x=..., y=...)

    # set frequecy
    >> ch.run(freq=1000)

    # set delay
    >> ch.run(delay=0.05)

    """
    def __init__(self, **kwargs):

        # enable logging
        loglevel = logging.DEBUG if 'verbose' in kwargs and kwargs['verbose'] == True else logging.INFO
        logging.basicConfig(format='[%(levelname)s] %(message)s', level=loglevel)

        # click position 
        self.x = None if 'x' not in kwargs else kwargs['x']
        self.y = None if 'y' not in kwargs else kwargs['y']

        ## sensitivity level for stopping
        self.SUPER = 0.01
        self.NORMAL = 0.05
        self.STUPID = 0.1

        self.mouse = PyMouse()

    def dist(self, a, b): 
        """calculate distance between two point in 2-D plane"""
        return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

    def run(self, **kwargs):
        """
        Options
        =======
        x, y: tuple
            mouse position

        sensitive: SUPER/NORMAL/STUPID

        delay: int/float
            in seconds

        freq: int/float
            clicks/second
        """

        sensitive = self.NORMAL if 'sensitive' not in kwargs else kwargs["sensitive"]
        delay = 1 if 'delay' not in kwargs else kwargs["delay"]

        ## override delay by setting freq
        if 'freq' in kwargs:
            delay = 1.0/freq

        x = self.x if 'x' not in kwargs else kwargs['x']
        y = self.y if 'y' not in kwargs else kwargs['y']

        if x is None or y is None:
            raise Exception("x and y must be given: run(x=..., y=...)")

        ## minimum distance to stop
        min_dist = max(self.mouse.screen_size())*sensitive

        self.mouse.move(x, y)

        logging.info('Ready to go!')
        prev = None
        while True:
            time.sleep(delay)
            current = self.mouse.position()
            if prev:
                d = self.dist(current, prev)
                if d > min_dist:
                    logging.debug('(%.2f, %.2f)-->(%.2f, %.2f): %.2f [stop]' % (prev[0], prev[1], current[0], current[1], d) )
                    break
                else:
                    logging.debug('(%.2f, %.2f)-->(%.2f, %.2f): %.2f [pass]' % (prev[0], prev[1], current[0], current[1], d) )
                    self.mouse.click(x, y, button=1, n=1) # Button is defined as 1 = left, 2 = right, 3 = middle.

            prev = current
            

if __name__ == '__main__':
    
    # from simple_click import ClickerHeroes

    import sys
    x, y = [1550, 585] if len(sys.argv) < 3 else map(lambda a:float(a), sys.argv[1:])
    ch = ClickerHeroes(x=x, y=y)
    ch.run(delay=0.05, freq=1000)
    

   