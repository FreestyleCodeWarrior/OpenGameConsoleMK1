from machine import Timer


class GameTimer:
    def __init__(self, driver, time_limit=None):
        self.driver = driver
        self.time_limit = time_limit
        if time_limit:
            self.init_countdown_timer()
        else:
            self.init_normal_timer()


    def init_countdown_timer(self):
        self.game_over = False
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
        minute = seconds // 60
        second = seconds % 60
        return "{:0>2}{:0>2}".format(minute, second)
    
    
    def show(self):
        self.driver.chars(self.encode(self.seconds))


    def start(self):
        self.timer = Timer(2)
        self.timer.init(mode=Timer.PERIODIC, period=1000, callback=self.callback)
        self.driver.segmode("7")
        self.show()

    def stop(self):
        self.timer.deinit()
        self.driver.segmode("8")
    

    def get_seconds_used(self):
        if self.time_limit:
            return (self.time_limit - self.seconds)
        else:
            return self.seconds
