# MicroPython version: v1.19.1 on 2022-06-18
# Espressif ESP32-WROOM-32


class GameTimer:
    def __init__(self, countdown):
        self.countdown = countdown
        if countdown:
            self._init_countdown_timer()
        else:
            self._init_normal_timer()


    def _init_countdown_timer(self):
        pass


    def _init_normal_timer(self):
        self.seconds = 0
        self.disp = self.encoder(self.seconds)


    def encoder(self):
        minute = self.seconds // 60
        second = self.seconds % 60
        return "{:0>2}{:0>2}".format(minute, second)
    
    def get_seconds_used(self):
        if self.countdown:
            return 
        else:
            return self.seconds
    
        
    
    