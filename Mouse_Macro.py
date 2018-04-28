import win32api
import win32con

class Mouse_Move:
    def __init__(self):
        self.xaxis=0
        self.yaxis-0
    def move_up(self,speed):
        win32api.mouse_event(win32con.MOUSE_MOVED, 0, -speed, 0, 0)
    def move_down(self,speed):
        win32api.mouse_event(win32con.MOUSE_MOVED, 0, speed, 0, 0)

    def move_right(self, speed):
        win32api.mouse_event(win32con.MOUSE_MOVED, speed, 0, 0, 0)

    def move_left(self, speed):
        win32api.mouse_event(win32con.MOUSE_MOVED, -speed, 0, 0, 0)
    def speed_processing(self,data):
        #data is tuple (r,p,y)
        #processing the data
        pass