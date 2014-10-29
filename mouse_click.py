import time
from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap


def mouseEvent(type, posx, posy):
        theEvent = CGEventCreateMouseEvent(None, type, (posx,posy), kCGMouseButtonLeft)
        CGEventPost(kCGHIDEventTap, theEvent)

def mousemove(posx,posy):
        mouseEvent(kCGEventMouseMoved, posx,posy);
        
def mouseclick(posx,posy):
        #mouseEvent(kCGEventMouseMoved, posx,posy); #uncomment this line if you want to force the mouse to MOVE to the click location first (i found it was not necesary).
        mouseEvent(kCGEventLeftMouseDown, posx,posy);
        mouseEvent(kCGEventLeftMouseUp, posx,posy);

from collections import namedtuple
MouseMove = namedtuple("MouseMove", ['name', 'posxy', 'times', 'sleep'])
def go_click(mouse_moves):
    if isinstance(mouse_moves, list):
        for i in range(mouse_moves[0]):
            for mouse_move in mouse_moves[1:]:
                go_click(mouse_move)
    elif isinstance(mouse_moves, MouseMove):
        for i in range(mouse_moves.times):
            time.sleep(0.03)
            print mouse_moves, i
            mouseclick(*mouse_moves.posxy)
        time.sleep(mouse_moves.sleep)

        
