# codingL utf-8

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

        logging.debug("loading PyMouse module...")
        self.mouse = PyMouse()
        logging.debug("PyMouse module loaded.")

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

        logging.debug("delay: %f" % (float(delay)) )
        logging.debug("sensitive: %f" % (float(sensitive)) )

        ## override delay by setting freq
        if 'freq' in kwargs and kwargs['freq']:
            if 1.0/freq < delay:
                delay = 1.0/freq

        x = self.x if 'x' not in kwargs else kwargs['x']
        y = self.y if 'y' not in kwargs else kwargs['y']

        if x is None or y is None:
            raise Exception("x and y must be given: run(x=..., y=...)")

        ## minimum distance to stop
        if 'screen' in kwargs:
            screen = kwargs['screen']
        else:
            self.mouse.screen_size()

        min_dist = max(screen)*sensitive

        logging.debug("the min distance is set as %.3f" % (float(min_dist)) )

        logging.debug("move mouse to %d, %d" % (int(x), int(y)) )
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
                    logging.info('Stop clicking!')
                    break
                else:
                    logging.debug('(%.2f, %.2f)-->(%.2f, %.2f): %.2f [pass]' % (prev[0], prev[1], current[0], current[1], d) )
                    self.mouse.click(x, y, button=1, n=1) # Button is defined as 1 = left, 2 = right, 3 = middle.

            prev = current

def usage():
    print 'python %s x y [options]' % (__file__)
    print 
    print 'x, y: the positions of mouse'
    print 
    print 'options:'
    print '  -d, --delay :   the delay between each click (in seconds)'
    print '  -f, --freq  :   the frequecy of click per second'
    print '  -h, --help  :   display help messages'
    print '  --verbose   :   show debug messages'
    exit(-1)

if __name__ == '__main__':
    
    # from simple_click import ClickerHeroes

    import sys, getopt
    if len(sys.argv) < 3:
        usage()
    else:
        x, y = map(lambda a:float(a), sys.argv[1:3])
        try:
            opts, args = getopt.getopt(sys.argv[3:],'hd:f:',['help','delay=', 'freq=', 'verbose'])
        except getopt.GetoptError:
            usage()

        ### read options
        verbose, freq, delay = False, 1, 0.05
        for opt, arg in opts:
            if opt in ('-h', '--help'): usage()
            elif opt in ('-d','--delay'): delay = float(arg.strip())
            elif opt in ('-f','--freq'): freq = float(arg.strip())
            elif opt in ('--verbose',): verbose = True

        ch = ClickerHeroes(verbose=verbose)
        ch.run(x=x, y=y, delay=delay, freq=freq, screen=(1440, 900))

   