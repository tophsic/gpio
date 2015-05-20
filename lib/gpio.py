


class Monitoring:
    'Gpio util for my own purpose'


    
    def __init__(self, parent_screen):
        maxyx = parent_screen.getmaxyx()
        screen = parent_screen.subwin(4, 15, maxyx[0] - 4, maxyx[1] - 15)
        screen.box()
        screen.refresh()
        self.screen = screen
