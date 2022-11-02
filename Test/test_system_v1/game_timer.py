from machine import Timer


class GameTimer:
    def __init__(self, driver, time_limit=None):
        self.driver = driver
        self.time_limit = time_limit
        self.game_over = False
        self.game_pause = False
        if time_limit:
            self.init_countdown_timer()
        else:
            self.init_normal_timer()
        self.encode(self.seconds)


    def init_countdown_timer(self):
        self.seconds = self.time_limit
        self.callback = self.count_down


    def init_normal_timer(self):
        self.seconds = 0
        self.callback = self.count_up


    def count_down(self, _):
        self.seconds -= 1
        if self.seconds == 0:
            self.game_over = True
            self.stop()
        self.show()


    def count_up(self, _):
        self.seconds += 1
        self.show()
    
    
    def encode(self, seconds):
        self.encoded_seconds = "{:0>2}{:0>2}".format(seconds // 60, seconds % 60)
    
    
    def show(self):
        self.encode(self.seconds)
        self.driver.chars(self.encoded_seconds)


    def start(self):
        self.timer = Timer(2)
        self.timer.init(mode=Timer.PERIODIC, period=1000, callback=self.callback)
        self.driver.segmode("7")
        self.show()


    def stop(self):
        self.timer.deinit()
        self.driver.segmode("8")
    
    
    def interrupt(self, mode):
        if mode == "quit":
            self.game_over = True
        elif mode == "pause":
            self.game_pause = True
        elif mode == "resume":
            self.game_pause = False
    

    def get_seconds_used(self):
        if self.time_limit:
            return (self.time_limit - self.seconds)
        else:
            return self.seconds
