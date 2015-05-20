


import time
from threading import Thread



class Counter(Thread):
    'Counter display on a screen'



    def __init__(self, screen):
        Thread.__init__(self)
        self.screen = screen
        self.terminated = False



    def run(self):
        i = 0

        while not self.terminated:
            self.screen.addstr(1, 1, str(i))
            i = i + 1
            self.screen.refresh()
            time.sleep(1)


    def stop(self):
        self.terminated = True
